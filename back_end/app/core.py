import couchdb
from app.constant import DB_Name, TwitterDataType, MastodonDataType

def get_doc_name_and_view_from_type(db_name, type):
    if db_name == DB_Name.TWITTER:
        if type == TwitterDataType.STATE:
            return ("state", "state_view")
    elif db_name == DB_Name.MASTODON:
        if type == MastodonDataType.RELATED_TOOTS:
            return ("count", "relatetoot")
        elif type == MastodonDataType.RELATED_USERS:
            return ("count", "relateusr")

def connect_to_db(db_name):
    couch = couchdb.Server('http://admin:admin@172.26.129.56:5984')

    try:
        print(couch[db_name])
        return couch[db_name]
    except couchdb.ResourceNotFound:
        print(f"Database '{db_name}' does not exist.")
        exit()
        return None

def get_sudo_data():
    db = connect_to_db(DB_Name.SUDO1.value)
    data_from_couch_db = []
    for doc_id in db:
        doc = db[doc_id]
        data_from_couch_db.append(doc["properties"])
    
    return data_from_couch_db 

def get_aggregated_data(db_name, type):
    db = connect_to_db(db_name.value)
    (doc, view_name) = get_doc_name_and_view_from_type(db_name, type)
    view_result = db.view(f'_design/{doc}/_view/{view_name}', group=True)

    result = []
    for row in view_result:
        result.append({ "key": row.key, "value": row.value })
    return result

def fetch_data(db_name, type = None):
    if db_name == DB_Name.SUDO1:
        return get_sudo_data()
    elif db_name == DB_Name.TWITTER and type is not None:
        return get_aggregated_data(db_name, type)
    
    return None
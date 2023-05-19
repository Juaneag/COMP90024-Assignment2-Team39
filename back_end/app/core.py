import couchdb
from app.constant import DB_Name

def connect_to_db(db_name):
    couch = couchdb.Server('http://admin:admin@172.26.129.56:5984')

    try:
        return couch[db_name]
    except couchdb.ResourceNotFound:
        print(f"Database '{db_name}' does not exist.")
        exit()
        return None

def get_sudo_data(db_name):
    db = connect_to_db(db_name.value)
    data_from_couch_db = []
    for doc_id in db:
        doc = db[doc_id]
        data_from_couch_db.append(doc["properties"])
    
    return data_from_couch_db 

def get_aggregated_data(db_name, type):
    db = connect_to_db(db_name.value)
    doc_and_view = get_doc_name_and_view_from_type(db_name, type)
    if doc_and_view == None:
        return None
    
    view_result = db.view(f'_design/{doc_and_view[0]}/_view/{doc_and_view[1]}', group=True)

    result = []
    for row in view_result:
        result.append({ "key": row.key, "value": row.value })
    return result

def fetch_data(db_name, type = None):
    if (db_name == DB_Name.TWITTER or db_name == DB_Name.MASTODON) and type is not None:
        return get_aggregated_data(db_name, type)
    
    return get_sudo_data(db_name)
import couchdb

def connectToDB():
    couch = couchdb.Server('http://admin:admin@172.26.136.129:5984')
    # couch = couchdb.Server('http://admin:1234@localhost:5984')
    db_name = 'st-map-test-data'

    try:
        return couch[db_name]
    except couchdb.ResourceNotFound:
        print(f"Database '{db_name}' does not exist.")
        exit()
        return None

def getLocationData(db):
    data_from_couch_db = []
    for doc_id in db:
        doc = db[doc_id]
        data_from_couch_db.append(doc["location"])
    
    return data_from_couch_db






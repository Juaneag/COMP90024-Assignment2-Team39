import couchdb
import ijson

couch = couchdb.Server()

couch = couchdb.Server('http://admin:admin@172.26.136.129:5984/')
#db = couch.create('twitter') 

db = couch["twitter"]
with open('../mnt/preprocessed_zip.json') as f:
    items = ijson.items(f, 'data.item')
    for record in items:
        print(type(record))
        #db.save(record)
        break

import couchdb2 as couchdb
import simplejson as json
import ijson
import time
from uuid import uuid4

begin = time.time()

couch = couchdb.Server()
couch = couchdb.Server('http://admin:admin@172.26.129.56:5984/')

db = couchdb.Database(couch, 'twitter')
print('connected')

path = 'preprocessed.json'
    

       
with open(path, 'r') as f:
    items = ijson.items(f, 'item')
    count = 1
    update_list = []
    for record in items:
        update_list.append(record)
        count += 1
        if count % 10000 == 0:
            print(count // 10000, 'round, data uplaoded is: ', count)
            db.update(update_list)
            print('time used so far is: ', time.time() - begin, ' secs')
            update_list = []
            
end = time.time()
#print(end - begin)
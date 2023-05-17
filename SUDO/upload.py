import couchdb2 as couchdb
import simplejson as json
import ijson
import time
from uuid import uuid4

begin = time.time()

couch = couchdb.Server()
couch = couchdb.Server('http://admin:admin@172.26.129.56:5984/')

db = couchdb.Database(couch, 'sudo')
print('connected')

path = 'SUDO.json'


with open(path, 'r') as f:
    items = ijson.items(f, 'features.item')

    for i in items:
        i = json.loads(json.dumps(i))
        i['_id'] = uuid4().hex
        db.put(i)
            
end = time.time()
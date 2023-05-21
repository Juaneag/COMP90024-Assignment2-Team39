# Use package: couchdb2 https://pypi.org/project/CouchDB2/
# simplejson https://pypi.org/project/simplejson/
# ijson https://pypi.org/project/ijson/
# uuid https://docs.python.org/3/library/uuid.html suggested by couchdb package documentation https://couchdb-python.readthedocs.io/en/latest/client.html#database

import couchdb2 as couchdb
import simplejson as json
import ijson
import time
from uuid import uuid4

begin = time.time() # to record time

# variables
COUCHDB_MASTER_NODE = 'http://admin:admin@172.26.129.56:5984/'
DATA_BASE = 'sa2'
path = 'SUDO3.json'

# connect to couchDB server and database
couch = couchdb.Server()
couch = couchdb.Server(COUCHDB_MASTER_NODE)

db = couchdb.Database(couch, DATA_BASE)
print('connected')

# import data
with open(path, 'r') as f:
    items = ijson.items(f, 'features.item')

    for i in items:
        i = json.loads(json.dumps(i))
        i['_id'] = uuid4().hex
        db.put(i)
            
end = time.time()
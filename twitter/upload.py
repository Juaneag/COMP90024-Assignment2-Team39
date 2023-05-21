# used package: couchdb2 https://pypi.org/project/CouchDB2/
# ijson https://pypi.org/project/ijson/
############################################################
# get idea from ED discussion: https://edstem.org/au/courses/11705/discussion/

import couchdb2 as couchdb
import ijson
import time

# variables
COUCHDB_MASTER_NODE = 'http://admin:admin@172.26.129.56:5984/'
DATA_BASE = 'twitter'
path = 'preprocessed.json'

'''
import twitter data to couchDB. Print current state while running
'''
# connect to couchdb server and database
begin = time.time()

couch = couchdb.Server()
couch = couchdb.Server(COUCHDB_MASTER_NODE)

db = couchdb.Database(couch, DATA_BASE)
print('connected')



       
with open(path, 'r') as f:
    items = ijson.items(f, 'item')
    count = 1
    update_list = []
    for record in items:
        update_list.append(record)
        count += 1
        # update 10000 records a time
        if count % 10000 == 0:
            print(count // 10000, 'round, data uplaoded is: ', count)
            db.update(update_list)
            print('time used so far is: ', time.time() - begin, ' secs')
            update_list = []
            
end = time.time()
#print(end - begin)
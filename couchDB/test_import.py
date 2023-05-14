import couchdb2 as couchdb
import simplejson as json
import ijson
import time
from uuid import uuid4

begin = time.time()

couch = couchdb.Server()
couch = couchdb.Server('http://admin:admin@172.26.136.129:5984/')

db = couchdb.Database(couch, 'hugedb')
print('connected')

path = '../mnt/preprocessed_zip.json'

def get_upload_doc(input):
    uid = input['doc']['data']['author_id']
    text = input['doc']['data']['text']
    place = input['doc']['includes']['places'][0]['full_name']
    tokens = input['value']['tokens']
    out_dic = {}
    out_dic['_id'] = uuid4().hex
    out_dic['uid'] = uid
    out_dic['text'] = text
    out_dic['place'] = place
    out_dic['tokens'] = tokens
    return out_dic
    

       
with open(path,"r",encoding='utf-8') as f:
    items = ijson.items(f, 'data.item')
    count = 1
    update_list = []
    for record in items:
        #record = json.loads(json.dumps(record))
        #update_list.append(record)
        try:
            record = get_upload_doc(record)
            update_list.append(record)
        except:
            pass
        count += 1
        if count % 10000 == 0:
            print(count // 10000, 'round, data uplaoded is: ', count)
            db.update(update_list)
            print('time used so far is: ', time.time() - begin, ' secs')
            update_list = []
            
end = time.time()
#print(end - begin)
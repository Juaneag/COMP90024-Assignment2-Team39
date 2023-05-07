import ijson
import os

os.remove('../mnt/preprocessed.json')

out = open('../mnt/preprocessed.json', 'a')
out.write('{\"data\": [')
count = 1

with open('../mnt/ext100/twitter-huge.json') as f:
    items = ijson.items(f, 'rows.item.doc')
    for item in items:
        preprocessed_dict = {}
        for record in items:
            try:
                id = record['data']['author_id']
                place = record['includes']['places'][0]['full_name'].split(',')[0].lower()
                js_out = '{\"author_id\": \"' + id + '\", \"place\": \"' + place + '\"}'
                if count != 1:
                    out.write(', \n')
                out.write(js_out)
                count += 1
            except:
                continue
            #if count == 10:
                #break
        #if count == 10:
            #break


out.write('], \"count\": \"' + str(count) + '\"}')          
out.close()
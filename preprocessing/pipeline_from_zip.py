'''
Refer to official document: https://docs.python.org/3/library/zipfile.html#zipfile-objects and 
online resources: https://stackoverflow.com/questions/40824807/reading-zipped-json-files
'''
import ijson
from zipfile import ZipFile
import os

try:
    os.remove('../mnt/preprocessed_zip.json')
except:
    pass

out = open('../mnt/preprocessed_zip.json', 'a')
out.write('{\"data\": [')
count = 1

with ZipFile('../twitter-huge.json.zip', 'r') as zip:
    with zip.open(zip.namelist()[0]) as f:
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
                # if count == 10:
                    # break
            # if count == 10:
                # break

out.write('], \"count\": \"' + str(count) + '\"}')          
out.close()  

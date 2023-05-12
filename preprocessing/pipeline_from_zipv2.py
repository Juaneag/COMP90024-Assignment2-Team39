'''
--- Changes for this version ---
- change to save in txt format, as saved format no longer a valid json format
- removed the open and end line, only take tweet object
'''
import ijson
import simplejson as json
from zipfile import ZipFile
import os

output_path = '../preprocessed_zip.txt'

try:
    os.remove(output_path)
except:
    pass

out = open(output_path, 'a')
count = 1

def check_keywords(text, keywords):
    found_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_keywords.append(keyword)
    return found_keywords

with ZipFile('../twitter-huge.json.zip', 'r') as zip:
    with zip.open(zip.namelist()[0]) as f:
        items = ijson.items(f, 'rows.item')
        for record in items:
            try:
                id = record['doc']['data']['author_id']
                place = record['doc']['includes']['places'][0]['full_name']
                js_out = json.dumps(record)
                if count != 1:
                    out.write(', \n')
                out.write(js_out)
                count += 1
            except:
                continue
out.close()  

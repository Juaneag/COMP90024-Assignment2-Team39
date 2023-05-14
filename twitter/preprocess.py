'''
--- Changes for this version ---
- change to save in txt format, as saved format no longer a valid json format
- removed the open and end line, only take tweet object
'''

import sys
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import couchdb2 as couchdb
from uuid import uuid4
import ijson
import simplejson as json
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from zipfile import ZipFile
import os
nltk.download('punkt')
nltk.download('stopwords')


keywords = ["voluntary", "volunteer", "volunteering", "nonprofit", "charity", "donor", "donation", "unpaid", "rendering", "bestowing", "volitional"]
porterStemmer = PorterStemmer()
keywords = set([porterStemmer.stem(w) for w in keywords])
stop_words = set(stopwords.words('english'))

def nlp_content(content):
    out = re.sub(r'non-profit', 'nonprofit', content.lower())
    out = re.sub(r'https:\/\/[^\s]+', '', out) # remove link
    out = re.sub(r'[^A-z\s]', ' ', out) # remove all english character words
    out = re.sub(r'\s+', ' ', out) # deal with multiple space

    tokens = nltk.word_tokenize(out) # tokenisation

    # stop words removal
    no_stop_words = [w for w in tokens if w not in stop_words]

    # Stemming
    stemmed = [porterStemmer.stem(w) for w in no_stop_words]
    
    return stemmed

def determine_related(content):
    for w in content:
        if w in keywords:
            return True
    return False

def convert_record(record):
    try:
        uid = record['doc']['data']['author_id']
        place = record['doc']['includes']['places'][0]['full_name'].split(',')[0].lower()
        lang = record['doc']['data']['lang']
        state = -1
        for k, v in state_dict.items():
            if place in v:
                state = k
                break
        if state == -1 or lang != 'en':
            return False
    except:
        return False
    #try:
        #tags = [porterStemmer.stem(w['name']) for w in record['tags']]
    #except:
        #tags = []
    #try:
        #time = record['created_at']
    #except:
        #time = 'null'
    try:
        #original_content = BeautifulSoup(record['doc']['data']['text'], 'html.parser').text
        original_content = record['doc']['data']['text']
        content = nlp_content(original_content)
        related = 0 if not determine_related(content=content) else 1
    except:
        original_content = ''
        related = 0
    out = dict()
    out['uid'] = uid
    out['content'] = original_content
    out['place'] = place
    out['state'] = state
    out['related'] = related
    return out

with open('data/sal.json') as fsal:
    sal_items = ijson.items(fsal, '')
    state_dict = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
    for item in sal_items:
        for k, v in item.items():
            state_dict[v['ste']].append(k)




output_path = 'preprocessed.json'

try:
    os.remove(output_path)
except:
    pass



out = open(output_path, 'a')
out.write('[')
count = 1

with ZipFile('data/twitter-huge.json.zip', 'r') as zip:
    with zip.open(zip.namelist()[0]) as f:
        items = ijson.items(f, 'rows.item')
        for record in items:
            record = convert_record(record)
            if record != False:
                js_out = json.dumps(record)
                if count != 1:
                    out.write(', \n')
                out.write(js_out)
                count += 1
                if count % 10000 == 0:
                    print(count, 'has been dealt with')
out.write(']')
out.close()  

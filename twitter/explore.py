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


path = 'preprocessed.json'

with open(path,"r",encoding='utf-8') as f:
    items = ijson.items(f, 'item')
    count = 1
    count_related = 0
    for record in items:
        #content = nlp_content(record['content'])
        #print(content)
        #related = 0 if not determine_related(content=content) else 1
        #print(related)
        if record['related'] == 1:
            #print(1)
            count_related += 1
        #if count % 100000 == 0:
            #print(count)
            #break
            #if record['related'] == 0:
                #print(type(record['related']))
        #break
        count += 1
    print(count)
    print(count_related)
    print(count_related/count * 100)
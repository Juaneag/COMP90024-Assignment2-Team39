# beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
# online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object
# workshop solution from past course: https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
# regular expression document: https://www.w3schools.com/python/python_regex.asp
# keywords from: https://www.merriam-webster.com/thesaurus/volunteer
# sys argvs trick by: https://www.youtube.com/watch?v=EYNwNlOrpr0
# couchdb package documentation: https://pypi.org/project/CouchDB2/
###########################################################################################################################################################################
# NB: Need to pass in sys argv, e.g. 'https://mastodon.au'

import sys
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import couchdb2 as couchdb
from uuid import uuid4
import json
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
nltk.download('punkt')
nltk.download('stopwords')


couch = couchdb.Server()

couch = couchdb.Server('http://admin:admin@172.26.129.56:5984/')

db = couchdb.Database(couch, 'mastodon')

m = Mastodon(api_base_url=sys.argv[1], access_token=sys.argv[2])

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
        uid = record['account']['id']
        usr_name = record['account']['username']
        try:
            usr_note = record['account']['note']
        except:
            usr_note = ''
        original_content = BeautifulSoup(record['content'], 'html.parser').text
        content = nlp_content(original_content)
        related = 0 if not determine_related(content=content) else 1
        related_usr = 0 if not determine_related(content=usr_note) else 1
    except:
        return False
    try:
        tags = [porterStemmer.stem(w['name']) for w in record['tags']]
    except:
        tags = []
    try:
        time = record['created_at']
    except:
        time = 'null'
    out = dict()
    out['uid'] = uid
    out['user_name'] = usr_name
    out['content'] = original_content
    out['tags'] = tags
    out['time'] = time
    out['related'] = related
    out['usr_related'] = related_usr
    return out

class Listener(StreamListener):
    def on_update(self, status):
        # deal with json file: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
        record = convert_record(status)
        if record != False:
            record['_id'] = uuid4().hex
            record = json.loads(json.dumps(convert_record(status), default=str))
            db.put(record)


m.stream_public(Listener())
    

# beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
# online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object
# workshop solution from past course: https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
# regular expression official document: https://www.w3schools.com/python/python_regex.asp
# keywords from: https://www.merriam-webster.com/thesaurus/volunteer

import json
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet 
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

keywords = ["voluntary", "volunteer", "volunteering", "nonprofit", "charity", 
            "donor", "donation", "unpaid", "rendering", "bestowing", "volitional"]


porterStemmer = PorterStemmer()
keywords = set([porterStemmer.stem(w) for w in keywords])
stop_words = set(stopwords.words('english'))

def nlp_content(content):
    out = re.sub(r'https:\/\/[^\s]+', '', content.lower()) # remove link
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
        original_content = BeautifulSoup(record['content'], 'html.parser').text
        content = nlp_content(original_content)
        related = 0 if not determine_related(content=content) else 0
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
    return out

with open('example.json', 'r') as f:
    data = json.load(f)
    for record in data:
        out = convert_record(record)
        #print(out)
        
print(keywords)
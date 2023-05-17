# archived

import json
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet 
from couchdb import Server, Document
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
    out = re.sub(r'@(\w+)', '', out) # remove mentions
    out = re.sub(r'[^A-z\s]', ' ', out) # remove all english character words
    out = re.sub(r'\s+', ' ', out) # deal with multiple space
    tokens = nltk.word_tokenize(out) # tokenisation

    # stop words removal
    no_stop_words = [w for w in tokens if w not in stop_words]

    # Stemming
    stemmed = [porterStemmer.stem(w) for w in no_stop_words]
    
    return stemmed

def check_keywords(tokens):
    matched_words = []
    for w in tokens:
        if w in keywords:
            matched_words += [w]
    return matched_words

def upload_twitter_data(file_path: str, batch_size: int, couchdb_endpoint: str, database: str)-> None:
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
        
    db = couch[database]
    records = []
    i=0
    onlyFilteredConver = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith(", \n"):
                line = line[:-3]
            tweet = json.loads(line)
            tweet_tags = tweet["value"]["tags"].split("|")
            tweet_tokens = tweet["value"]["tokens"].split("|")
            tweet_tokens_and_tags = tweet_tokens + tweet_tags
            content = tweet["doc"]["data"]["text"]
            
            tokens = nlp_content(content)

            if len(check_keywords(tweet_tokens_and_tags + tokens)) > 0:
                content = tweet["doc"]["data"]["text"]
                list = content.split(" ")
                removedMention = []
                for i in list:
                    if str(i).startswith('@') == False:
                        removedMention.append(i)
                removedMentionStr = ' '.join(removedMention)
                onlyFilteredConver.append(removedMentionStr)
        records.append(Document({"aggregated_conver": onlyFilteredConver}))
        if len(records) > 0:
            db.update(records)
def main(): 
    file_path = '../preprocessed_zip.txt'
    couchdb_endpoint = 'http://admin:admin@172.26.136.129:5984'
    batch_size = 5000
    couchdb_database = 'content-twitter'

    upload_twitter_data(file_path,batch_size, couchdb_endpoint, couchdb_database)
    
if __name__ == "__main__":
    main()
import json
from couchdb import Server, Document

keywords = ["volunteer", "volunteering", "nonprofit", "charity", "donor", "donation"]

def check_keywords(text, keywords):
    matched_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            matched_keywords.append(keyword)
    return matched_keywords

def upload_twitter_data(file_path: str, batch_size: int, couchdb_endpoint: str, database: str)-> None:
    couch = Server(couchdb_endpoint)
    if database not in couch:
        couch.create(database)
        
    db = couch[database]
    records = []
    i=0
    countMatchedKeywords = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith(", \n"):
                line = line[:-3]
            obj = json.loads(line)
            
            if check_keywords(line, keywords):
                countMatchedKeywords += 1
                records.append(Document({ "tweet" : obj }))

            if len(records)!=0 and len(records) % batch_size == 0:
                print(f"processed {i} records")
                db.update(records)
                records = []
            i += 1
        if len(records) > 0:
            db.update(records)
        print(f'Matched {countMatchedKeywords} tweets')
def main(): 
    file_path = '../preprocessed_zip.txt'
    batch_size = 5000
    couchdb_endpoint = 'http://admin:admin@172.26.136.129:5984'
    couchdb_database = 'filtered-tweets'

    upload_twitter_data(file_path,batch_size, couchdb_endpoint, couchdb_database)
    
if __name__ == "__main__":
    main()
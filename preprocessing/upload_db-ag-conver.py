import json
from couchdb import Server, Document

shouldRemoveMention = False 
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
    onlyFilteredConver = []
    countMatchedKeywords = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith(", \n"):
                line = line[:-3]
            
            obj = json.loads(line)
            if check_keywords(line, keywords):
                content = obj["doc"]["data"]["text"]
                list = content.split(" ")
                if (shouldRemoveMention):
                    removedMention = []
                    for i in list:
                        if str(i).startswith('@') == False:
                            removedMention.append(i)
                    removedMentionStr = ' '.join(removedMention)
                    onlyFilteredConver.append(removedMentionStr)
                else:
                    onlyFilteredConver.append(content)

        records.append(Document({"aggregated_conver": onlyFilteredConver}))

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
# 16 May Update
## Streamlit (frontend)
- add map (retrieve mock data from couchDB)
- add stackedBar with mock data

# 11 May Update
## CouchDB
- update preprocessing data code, added v2
- add code for upload data to DB
- upload data to test db
    - filtered-tweets by upload_db
        - filtered with keywords
        - saved each tweet per record in json format
    - conver-tweets by upload_db-ag-conver (just for see overall content selected keywords)
        - filtered with words, take only content, aggregated to list
        - saved one list of all contents contained keywords in a record

# 10 May Update
## frontend
- add template for streamlit, consists of pages and board displays data from couchDB
- update dockerfile
- add docker-compose file, run on port 8501

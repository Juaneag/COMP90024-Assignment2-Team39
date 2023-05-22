# 22 May
## Frontend
- For combine realted page, fix stacked line graph to combined line graph, and add stacked bar instead
- Refactor

# 21 May
## Frontend
- Refactor and fix overlap label for combine related chart
- Fix stacked bar showing incorrect data for showing more than 2 type of data
- Redeploy frontend

# 20 May
## Frontend
- Add map, stacked bar, bar charts
- Deploy frontend
- Update note and readme

# 19 May
## Backend
- add note for sudo data detail and its fields
- add endpoints to fetch data and views from couchDB
    - sudo, twitter, mastodon

# 18 May
## Backend
- deploy to server successfully

# 17 May
## Backend
- add backend code, use flask
- add docker-compose file
- currently, work with http://localhost:8296/healthcheck

# 16 May
## Streamlit (frontend)
- add map (retrieve mock data from couchDB)
- add stackedBar with mock data

# 11 May
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

# 10 May
## Frontend
- add template for streamlit, consists of pages and board displays data from couchDB
- update dockerfile
- add docker-compose file, run on port 8501

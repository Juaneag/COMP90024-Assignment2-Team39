# Twitter

## Introudction

In this floder, only aim is to deal with twitter data. Preprocess twitter data, then import to couchDB.

The data is given in dropbox, which is over 12 GiB as zip file and over 60 GiB as json file.

## Table of contents

- [Twitter](#twitter)
  - [Introudction](#introudction)
  - [Table of contents](#table-of-contents)
  - [How to run](#how-to-run)
  - [Rule](#rule)
  - [Discussion](#discussion)
    - [NLP](#nlp)
    - [Import](#import)
    - [Whole Process](#whole-process)
  - [Acknowledgement and Reference](#acknowledgement-and-reference)

## How to run

- make sure twitter data is in following path and ***DON'T UNZIP IT***, OR change INPUT_PATH in preprocess to the zip file: 
  ```
  ./data/twitter-huge.json.zip
  ```
- change IP address of master node of couchDB in upload.py
    ```python
    COUCHDB_MASTER_NODE = 'http://admin:admin@{IP}:5984/'
    ```
    where {IP} is IP of couchDBMaster
- in terminal, run:
  ```bash
  python3 preprocess.py
  ```
  The preprocessed.json file will be created, if already exists, will be cleared and write preprocessed twitter data.
- in terminal, run:
  ```bash
  python3 upload.py
  ```
  to upload twitter data onto couchDB

-----------------------------------------

On instance:

It is also possible to run the twitter data process and import to couchDB on instances:

- copy script to instance by scp
- download twitter data on instance through wget
- run exact same process above.


## Rule

In database, only have info:

- user id
- content
- place
- state: this is determined by assignment 1 sal.json file under BingguangL's assumption
- related: 1 is related 0 is not

## Discussion 

### NLP

Same process as [mastodon](../mastodon/README.md#discussion-nlp)

### Import

Suggested by response of ED Discussion fourm.

Split preprocessed.json into parts, each part contain 10000 records. Upload one part once instead of upload one record once to increase efficiency.

### Whole Process

Consider twitter data is past data will not change in size, content. Hence, it doesn't matter where to deploy this process. Our choice is to do it loaclly since the twitter data is not huge. 

If twitter data size increase a lot, i.e. more than hundurds GiB, then better to run it on instance with volume mounted to.

## Acknowledgement and Reference

Similar to [mastodon](../mastodon/README.md#acknowledgement-and-reference)

- workshop solution from past course: https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
- regular expression document: https://www.w3schools.com/python/python_regex.asp
- keywords from: https://www.merriam-webster.com/thesaurus/volunteer
- couchdb package documentation: https://pypi.org/project/CouchDB2/
  and https://couchdb-python.readthedocs.io/en/latest/client.html#database
- ED discussion: https://edstem.org/au/courses/11705/discussion/
- deal with zip file: https://stackoverflow.com/questions/40824807/reading-zipped-json-files
- convert decimal in json: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable and https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
- used sal.json provided in Assignment 1
- used Bingguang and Arezoo's code for Assignment 1


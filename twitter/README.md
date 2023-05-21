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

- make sure twitter data is in following path and ***DON'T UNZIP IT***: 
  ```
  ./data/twitter-huge.json.zip
  ```
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

Consider twitter data is past data will not change in size, content. Hence, it doesn't matter where to deploy this process. Our choose is to do it loaclly considered to the hardware.

## Acknowledgement and Reference

Similar to [mastodon](../mastodon/README.md#acknowledgement-and-reference)

- beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
- online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object
- workshop solution from past course: https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
- regular expression document: https://www.w3schools.com/python/python_regex.asp
- keywords from: https://www.merriam-webster.com/thesaurus/volunteer
- couchdb package documentation: https://pypi.org/project/CouchDB2/
  and https://couchdb-python.readthedocs.io/en/latest/client.html#database
- ED discussion: https://edstem.org/au/courses/11705/discussion/
- deal with zip file: https://stackoverflow.com/questions/40824807/reading-zipped-json-files
- convert decimal in json: https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
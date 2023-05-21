# Mastodon

## Introduction

***Note:*** Dockerfile, MastodonStream.py is exact same as the one in [ansible playbook](../ansible/README.md#how-to-run).

## Table of contents

- [Mastodon](#mastodon)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [How to run](#how-to-run)
    - [By python script](#by-python-script)
    - [By docker](#by-docker)
      - [To run in ***mastdon\_harvester*** instance](#to-run-in-mastdon_harvester-instance)
    - [By Ansible Playbook](#by-ansible-playbook)
  - [Files](#files)
  - [Discussion](#discussion)
    - [NLP](#nlp)
    - [Import](#import)
  - [Acknowledgement and Reference](#acknowledgement-and-reference)

## How to run

### By python script

As described in python script documentation, when run python code, need to pass in the sys arg mastodon server url and access token:

```bash
python3 MastodonStream.py SERVER_URL ACCESS_TOKEN
```

This is not suggested as python script will run 'forever'.

### By docker

Note that Dockerfile is altered to cope with Ansible Playbook

#### To run in [***mastdon_harvester***](../ansible/README.md#mastodon) instance

In this case, only consider the situation when harvester is down for some reason and need reboot:

- Login to instance by
  ```bash
  ssh -i KEY_PATH ubuntu@IP_ADDRESS
  ```
- In terminal, run:
  ```bash
  sudo docker ps -a
  ```
  find the exited container, get the container name
- In terminal, run:
  ```bash
  sudo docker start CONTAINER_NAME
  ```

To run this container locally or in new instances:

In this case, Dockerfile needed to be changed:

- Make sure MastodonStream.py is in same PATH with Dockerfile
- In Dockerfile, add one line:
  ```dockerfile
  CMD ["python", "./MastodonStream.py", "SERVER_URL", "ACCESS_TOKEN"]
  ```

***NOTE:*** In this case, each new harvester is need to change Dockerfile before deploy

### By Ansible Playbook

Follow detailed instruction in [ansible README](../ansible/README.md#how-to-run), and the playbook is in [ansible floder](../ansible/mastodon/).

This is the suggested way to run this code.

## Files

- example.json: example of data stream from mastodon
- MastodonStream.py: script stream mastodon data, process with NLTK, add related tag, import to couchDB
- Dockerfile: to create image for harvester

## Discussion 

### NLP

For performance issue, our team decide to use NLTK to do only basic NLP on both Mastodon data and Twitter data. No model is trained and no pre-trained model is used.

For key-word dictionary, use [online tool](#https://www.merriam-webster.com/thesaurus/volunteer) to find synonyms. Not use NLTK to find synonyms since it is more suitable for model training than our aim. In our case, it will return many unreasonable value e.g., furnish, which later NLTK process will link to furniture.

### Import

Decision on the way to import data into couchDB is:

1. stream data, store in memory (RAM)
2. process data as described [above](#discussion-nlp)
3. straight import to couchDB

Which means import data one by one. This would not use any disk space on [***mastodon_harvester***](../ansible/README.md#mastodon) and hence more flexibility when scale up.

## Acknowledgement and Reference

- beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
- online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object
- workshop solution from past course in unimelb (COMP20008): https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
- regular expression documentation: https://www.w3schools.com/python/python_regex.asp
- keywords from: https://www.merriam-webster.com/thesaurus/volunteer
- sys argvs trick by: https://www.youtube.com/watch?v=EYNwNlOrpr0
- couchdb package documentation: https://pypi.org/project/CouchDB2/
  and https://couchdb-python.readthedocs.io/en/latest/client.html#database
- ED discussion: https://edstem.org/au/courses/11705/discussion/
- mastodon streamer code from course workshop repo: https://gitlab.unimelb.edu.au/feit-comp90024/comp90024
- deal with json file: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable and https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object

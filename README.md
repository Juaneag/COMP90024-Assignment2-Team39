# COMP90024-Assignment2-Team39
Team 39 Cloud computing assignment 2

## Table of Contents

- [COMP90024-Assignment2-Team39](#comp90024-assignment2-team39)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [How to use](#how-to-use)
  - [Discussions](#discussions)
  - [Acknowledgement and Reference](#acknowledgement-and-reference)

## Introduction

This is Team 39, Assignment 2 Project for Cloud Computing COMP90024. This project is designed to run on Melbourne Research Cloud (MRC).

-----

Front end page is accessible at: http://172.26.135.143:8501

***Note:*** to have access to above link, make sure you are on campus or otherwise connected to the University VPN (via Cisco AnyConnect)

------

There are 7 floders:

- [twitter](./twitter/) which deal with huge twitter data given in dropbox
- [mastodon](./mastodon/) which create one (or multiple) mastodon harvester(s)
- [SUDO](./SUDO/) which import SUDO data to couchDB
- [ansible](./ansible/) which create instance on MRC, deploy containers on instances. Will contain code in mastodon and couchDB
- [couchDB](./couchDB/) which contain command to set-up cluster manually and the code to create map-reduce view
- [back_end](./back_end/) which create the restful API for back end
- [front_end](./front_end/) which create the front end at above link

## How to use

This instruction only contains high level information to deploy the system, for detailed instruction, refer to the README file at each floder (will have link in this README):

- Logon to MRC, go to the right project. In Network, Security groups, create corresponding Security groups as described [here in step 3](./ansible/README.md#how-to-run).
- Setup couchDB cluster:
  - Create one instance as couchDB master node, name is couchDBMatser, record its IP.
  - Change variables accordingly as directed [here](./ansible/README.md#couchdb)
  - In terminal, go to _/ansible/couchDB/_:
    ```bash
    cd ansible/couchDB
    ```
  - Follow instruction on how to run Ansible notebook [here](./ansible/README.md#how-to-run)
- Deal with twitter data (stable zip/json file) and import to couchDB cluster created in previous step, detailed instruction is [here](./twitter/README.md#how-to-run)
  - go to correct floder:
    ```bash
    cd twitter
    ```
  - make sure data is in correct path, or the path variable is changed accordingly
  - change IP address of master node of couchDB (recoreded above) in upload.py as [directed](./twitter/README.md#how-to-run)
  - in terminal run:
    ```bash
    python3 preprocess.py
    ```
    and 
    ```bash
    python3 upload.py
    ```
  ***Note:*** the whole process might take a while, depend on the size of twitter data. Few times of the given huge twitter data size will work on this code (i.e. few hunduard GiB json/ 100 GiB zip file).
- Import SUDO data (stable json file) to couchDB cluster, detailed instruction is [here](./SUDO/README.md#how-to-run)
  - go to correct floder:
    ```bash
    cd SUDO
    ```
  - change IP address of master node of couchDB (recoreded above) in upload.py files as [directed](./SUDO/README.md#how-to-run)
  
    And make sure change the python script correspondingly as [instructed](./SUDO/README.md#how-to-run)
  - in terminal run:
    ```bash
    python3 upload.py
    ```
- Create one or more Mastodon harvester(s), process the data, import to couchDB cluster. The number is decided by user. Detailed instruction is [here](./ansible/README.md#how-to-run) and remember to [change variables](./ansible/README.md#mastodon)
  - go to correct floder:
    ```bash
    cd ansible/mastodon
    ```
  - change IP address of master node of couchDB (recoreded above) in upload.py files as described in [addinitional step](./ansible/README.md#addinitional-step)
  - make sure change the variable yaml file as [instructed](./ansible/README.md#mastodon)
  - Follow instruction on how to run Ansible notebook [here](./ansible/README.md#how-to-run)
- Create MapReduce View by method mentioned [here](./Mapreduce/)
- Create backend instance and deploy backend app:
  - Create instance for backend app, first go to corresponding floder, detailed instruction is [here](./ansible/README.md#how-to-run):
    ```bash
    cd ansible/backend
    ```
  - Follow instruction on how to run Ansible notebook [here](./ansible/README.md#how-to-run)
  - Create container for back_end, follow the detailed instruction [here](./back_end/README.md)
- Create frontend instance and deploy backend app:
  - Create instance for frontend app, first go to corresponding floder, detailed instruction is [here](./ansible/README.md#how-to-run):
    ```bash
    cd ansible/frontend
    ```
  - Follow instruction on how to run Ansible notebook [here](./ansible/README.md#how-to-run)
  - Create container for back_end, follow the detailed instruction [here](./front_end/README.md)

## Discussions

We give some discussions on sub-folder README file:

- [Ansible](./ansible/README.md#folders)
- [Mastodon harvester](./mastodon/README.md#discussion)
- [Twitter data process](./twitter/README.md#discussion)

## Acknowledgement and Reference

Refer to many documentations and sites, recorded in sub-folder README files. List some of them here:

- [Ansible](./ansible/README.md#acknowledgement-and-reference)
  <details>
    <summary>details</summary>

    All playbook is following workshop template repo:
    - Week 6 Workshop Recording and Slide: https://canvas.lms.unimelb.edu.au/courses/151783
    - Week 6 Workshop Repo By alwynpan (Yao Pan): https://canvas.lms.unimelb.edu.au/courses/151783

    Other:
    - ED discussion: https://edstem.org/au/courses/11705/discussion/
    - Code template to create docker image by playbook from: https://www.redhat.com/sysadmin/container-images-ansible
    - Ansible Documentation: https://docs.ansible.com/ansible/latest/index.html
    - Used suggested command to check if volume is mounted to instances: https://serverfault.com/questions/50585/whats-the-best-way-to-check-if-a-volume-is-mounted-in-a-bash-script
    - linux command line (mkdir -p PATH) follow instructions on https://www.javatpoint.com/linux-mkdir
    - Have conversion with ChatGPT on docker and ansible in genral level. 
  
    Suggestions on code by GPT:
    1. See _/roles/couchdb/tasks/main.yaml_ second block (chmod command for container mount). A brief description of the conversation on comment in the _yaml_ file.
    2. See _/roles/couchdb-cluser/tasks/main.yaml_ and _/roles/couchdb-cluser-finish/tasks/main.yaml_, change " to ' to make shell run.

    - Tried to use convert tool to convert curl command to ansible uri: https://curlconverter.com/ansible/
  
    However no code is used by output of the convert tool, use **ansible.builtin.shell** instead of **ansible.builtin.uri**

    </details>

- [Mastodon](./mastodon/README.md#acknowledgement-and-reference)
  <details>
    <summary>details</summary>

    - beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
    - online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object
    - workshop solution from past course: https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
    - regular expression documentation: https://www.w3schools.com/python/python_regex.asp
    - keywords from: https://www.merriam-webster.com/thesaurus/volunteer
    - couchdb package documentation: https://pypi.org/project/CouchDB2/
    and https://couchdb-python.readthedocs.io/en/latest/client.html#database
    - ED discussion: https://edstem.org/au/courses/11705/discussion/
    - mastodon streamer code from course workshop repo: https://gitlab.unimelb.edu.au/feit-comp90024/comp90024
    - deal with json file: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable and https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
  </details>

- [Twitter](./twitter/README.md#acknowledgement-and-reference): very similar to mastodon, only one not contained in mastodon:
  - deal with zip file: https://stackoverflow.com/questions/40824807/reading-zipped-json-files
  - used sal.json provided in Assignment 1
  - used Bingguang and Arezoo's code for Assignment 1

- [SUDO](./SUDO/README.md#acknowledgement-and-reference): very similar to twitter and mastodon.
- [Backend](./back_end/README.md#acknowledgement-and-reference)
  - For flask template, https://github.com/iliasmansouri/flask-swagger-template
  - For swagger format, https://swagger.io/docs/specification/2-0/basic-structure/
- [Frontend](./front_end/README.md#acknowledgement-and-reference)
  - For setup, https://docs.streamlit.io/library/get-started
  - Chart visualization
    - https://docs.streamlit.io/library/api-reference/charts
    - https://echarts.streamlit.app/
  - Calling API inside Streamlit
    - https://discuss.streamlit.io/t/using-an-api-from-inside-streamlit-app/37477/22
    - each request should have code running under main functions otherwise it will not working
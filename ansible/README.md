# Ansible

## Introduction

In this floder, contains 4 sub-floders:

- mastodon
- couchDB
- backend
- frontend

Each floder contains an Ansible playbook which create instance(s) on **Melbourne Research Cloud** (MRC). 

Each Ansible playbook expected to create instance(s), intsall docker on instance, create corresponding container(s) for the task.

## Table of Contents

- [Ansible](#ansible)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Environment](#environment)
  - [How to run](#how-to-run)
    - [Step 1](#step-1)
      - [Detailed Download Steps:](#detailed-download-steps)
    - [Step 2](#step-2)
      - [Detailed Steps:](#detailed-steps)
    - [Step 3](#step-3)
    - [Step 4](#step-4)
    - [Step 5](#step-5)
  - [Folders](#folders)
    - [mastodon](#mastodon)
      - [Functions](#functions)
      - [Scalable Instructions](#scalable-instructions)
    - [couchDB](#couchdb)
      - [Functions](#functions-1)
      - [Scalable Instructions](#scalable-instructions-1)
    - [backend](#backend)
    - [frontend](#frontend)
  - [Scalable Discussion](#scalable-discussion)
    - [Mastodon](#mastodon-1)
    - [couchDB](#couchdb-1)
    - [Frontend](#frontend-1)
  - [Acknowledgement and Reference](#acknowledgement-and-reference)












## Environment

- python version = 3.11.3
- ansible [core 2.14.5]



## How to run

Each floder has same process, here take [mastodon](#mastodon) as example.

### Step 1

Download openrc.sh file from MRC Dashboard. Put the openrc.sh file in the floder root path e.g., _./ansible/mastodon/openrc.sh._

<details>
<summary>Detailed instructions:</summary>

#### Detailed Download Steps:

1. login to MRC Dashboard on: https://dashboard.cloud.unimelb.edu.au/
2. select target project
3. in user tag on top right corner, download openstack RC file

</details>

### Step 2

Get the MRC API password.

<details>
<summary>Detailed instructions:</summary>

#### Detailed Steps:

1. in MRC Dashboard user, click settings
2. choose reset password option
3. get the API password

***WARNING***: Keep API password ***PRIVATE***

</details>

### Step 3

Make sure following Security Groups is already created and have **exact same** name:

- SSH: open port 22 ingress, for ssh login to the instance
- port4369: open port 4369 ingress, for couchDB cluster
- port5984: open port 5984 ingress, for couchDB cluster and couchDB Fauxton access
- port9100-9200: open ports 9100-9200 ingress, for couchDB cluster
- port8269: open port 8269 ingress, for backend
- port8501: open port 8501 ingress, for frontend

### Step 4

In ***hosts*** file, change path to ssh key and ansible user name accordingly. On MRC, ansible_user is by default _ubuntu_

```
ansible_ssh_private_key_file=~/PATH/TO/SSH_KEY_FILE
ansible_user=ubuntu
```

### Step 5

In Terminal, run:

```bash
./run-mrc.sh
```

Put the API key acquired above in the response

## Folders

### mastodon

#### Functions

The Playbook:
1. create one instance called ***mastodon_harvester***
2. install docker on the created instance
3. create and run container(s) to stream matodon data and import to couchDB

***NOTE:*** each container is aim for harvest one mastodon server, can create multiple containers to stream multiple server concurrently.

#### Scalable Instructions

To have multiple harvesters:

- In _/host_vars/mrc.yaml_, add name, accesstoken, and url of the wanted mastodon servers.

Then run the playbook as [instructions](#how-to-run) in above section.

### couchDB

#### Functions

The Playbook:
1. create one instance called ***couchDBMaster*** as master node of couchDB cluster
2. create two instances called ***couchDBCluster1*** and ***couchDBCluster2*** as couchDB nodes in cluster
3. also create volumes for all the three instances, mount to instance, change fstab to make volume auto mounted when reboot
4. install docker on all the three created instances
5. create and run couchdb containers on ***couchDBMaster***, ***couchDBCluster1***, and ***couchDBCluster2***, mount path to container
6. setup couchDB cluster

#### Scalable Instructions

To have different number of nodes:

- In _/host_vars/couchdb.yaml_, update the IP of the ***couchDBMaster*** instance
- In _/host_vars/mrc.yaml_, add/delete volumes to match desired number of nodes. Make sure to follow format: vol_name and vol_size
- In _/host_vars/mrc.yaml_, add/delete other_instances to match desired number of cluster nodes. Make sure to follow format: name and volumes, here volumes need to match the volume added in above step.

Then run the playbook as [instructions](#how-to-run) in above section.

***NOTE:*** When Need to know IP of the ***couchDBMaster*** so better way to run the playbook is to have ***couchDBMaster*** created beforehand, this could be done by run this playbook first part:
- In _mrc.yaml_, comment out any line hosts is ***not*** localhost

***NOTE:*** This is expected to run as first setup step of the whole app.

### backend

The Ansible playbook just create instance with proper security group. It can be extended to deploy whole backend app since it is already in container. Here are two ways:
- upload whole back_end floder onto instances, create container with dockerfile or docker compose.
- push image to docker hub, pull image in instance.

Our group choose second method. And in this case, no difference between deploy manually on instance or by playbook since only one backend app needed to deploy.

### frontend

Similar situation as backend.

## Scalable Discussion

### Mastodon

Note that any new harvester is a container and will be run in single instance ***mastodon_harvester***. Since Mastodon harvester container stream the data, single instance should be enough for this task. The ability to harvest more server can be done by one run.

### couchDB

Note that any new couchDB node is a container and will be run in brand new (its own) instance. The assumption is: this step is supposed to be done at first so no data already in couchDB cluster.

### Frontend

Since frontend is in own container, it is possible to shut down frontend and update. While couchDB, backend, harvester will not be effected.

## Acknowledgement and Reference

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

- All acknowledgement and Reference in Dockerfile and python script. Will be repeated in coresponding parts.
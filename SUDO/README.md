# SUDO

## Introduction

This floder, upload the SUDO data. No process is done, just upload.

## How to run

change IP address of master node of couchDB in upload.py
```python
COUCHDB_MASTER_NODE = 'http://admin:admin@{IP}:5984/'
```
where {IP} is IP of couchDBMaster

```bash
python3 upload.py
```

***NOTE:*** for different SUDO data, change DB name and data path in upload.py:
```python
DATA_BASE = 'TARGET_DB'
```
and 
```python
path = 'PATH_TO_SUDO_DATA'
```
make sure SUDO data is in same floder

## Acknowledgement and Reference

- couchdb package documentation: https://pypi.org/project/CouchDB2/
  and https://couchdb-python.readthedocs.io/en/latest/client.html#database
- deal with json file: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable and https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object

# SUDO

## Introduction

This floder, upload the SUDO data. No process is done, just upload.

## How to run

```bash
python3 upload.py
```

***NOTE:*** for different SUDO data, change DB name and data path in upload.py:
```python
db = couchdb.Database(couch, 'TARGET_DB')
```
and 
```python
path = 'PATH_TO_SUDO_DATA'
```
make sure SUDO data is in same floder

## Acknowledgement and Reference

- couchdb package documentation: https://pypi.org/project/CouchDB2/
  and https://couchdb-python.readthedocs.io/en/latest/client.html#database
- convert decimal in json: https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
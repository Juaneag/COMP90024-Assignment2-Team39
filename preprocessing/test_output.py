import json

with open('../mnt/preprocessed_zip.json', 'r') as f:
    item = json.load(f)
    
print(item['count'])
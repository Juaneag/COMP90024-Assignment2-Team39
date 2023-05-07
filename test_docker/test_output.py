import json

with open('../mnt/preprocessed.json', 'r') as f:
    item = json.load(f)
    
print(item['count'])
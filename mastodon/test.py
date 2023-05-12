# beautiful soup official documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
# online tutorial on getting text by beautiful soup: http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#converting-html-text-into-a-data-object

import json
import nltk
from bs4 import BeautifulSoup
import html2text

h = html2text.HTML2Text()
h.ignore_links = True

with open('example.json', 'r') as f:
    data = json.load(f)
    for record in data:
        try:
            uid = record['account']['id']
            usr_name = record['account']['username']
            content = record['content']
            language = record['language']
        except:
            continue
        try:
            tags = record['tags']
        except:
            tags = []

        soup = BeautifulSoup(content, 'html.parser')
        print(soup.text)
'''
--- Changes for this version ---
- change to save in txt format, as saved format no longer a valid json format
- removed the open and end line, only take tweet object
'''

# used material: workshop solution from past course in UniMelb (COMP20008): https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
# packages: ijson https://pypi.org/project/ijson/
# simplejson https://pypi.org/project/simplejson/
# nltk https://www.nltk.org/
# re https://docs.python.org/3/library/re.html
# zipfile https://docs.python.org/3/library/zipfile.html
# used sal.json provided in Assignment 1
# used Bingguang and Arezoo's code for Assignment 1
##########################################################
# Refer to: regular expression document: https://www.w3schools.com/python/python_regex.asp
# keywords from: https://www.merriam-webster.com/thesaurus/volunteer
# deal with zip file: https://stackoverflow.com/questions/40824807/reading-zipped-json-files
# convert decimal in json: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable and https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object


import ijson
import simplejson as json
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from zipfile import ZipFile
import os
nltk.download('punkt')
nltk.download('stopwords')

# variables
SAL_PATH = 'data/sal.json'
output_path = 'preprocessed.json'
INPUT_PATH = 'data/twitter-huge.json.zip'


# create keywords dictionary, do stemmer step by nltk
keywords = ["voluntary", "volunteer", "volunteering", "nonprofit", "charity", "donor", "donation", "unpaid", "rendering", "bestowing", "volitional"]
porterStemmer = PorterStemmer()
keywords = set([porterStemmer.stem(w) for w in keywords])
stop_words = set(stopwords.words('english'))

'''
get string content, do nlp process:
- clean the content string
- tokenize
- remove stop words
- stem
--------------------------------------
code adapt from previous course in uniMelb workshop solution:
https://edstem.org/au/courses/9158/lessons/25867/slides/185032/solution
--------------------------------------
Args:
    content (string): content need to process
Return:
    stemmed (list): a list of words processed as described above
'''
def nlp_content(content):
    out = re.sub(r'non-profit', 'nonprofit', content.lower())
    out = re.sub(r'https:\/\/[^\s]+', '', out) # remove link
    out = re.sub(r'[^A-z\s]', ' ', out) # remove all non-english character words
    out = re.sub(r'\s+', ' ', out) # deal with multiple space

    tokens = nltk.word_tokenize(out) # tokenisation

    # stop words removal
    no_stop_words = [w for w in tokens if w not in stop_words]

    # Stemming
    stemmed = [porterStemmer.stem(w) for w in no_stop_words]
    
    return stemmed

'''
determine if a tweet as related content
-----------------------------------------
rules: if content mentioned words in key-word dictionary,
it is related, otherwise is not
-----------------------------------------
Args:
    content (list): output of the nlp_content
Return:
    True/False (related/not related)
'''
def determine_related(content):
    for w in content:
        if w in keywords:
            return True
    return False

'''
convert raw tweet record to contain only information needed
----------------------------------------------------------
rules:
- each tweet record after process will contain:
    - user id
    - content: string value
    - place
    - state: matched by sal.json
    - related: as described above
- if tweet doesn't have any one of following, ignore:
    - user id
    - place
    - language is not 'en'
- if no place name matched in sal.json, ignore record
---------------------------------------------------------------------
Args:
    record: twitter data single record
Retrun:
    out: processed tweet
'''
def convert_record(record):
    try:
        uid = record['doc']['data']['author_id']
        place = record['doc']['includes']['places'][0]['full_name'].split(',')[0].lower()
        lang = record['doc']['data']['lang']
        state = -1
        for k, v in state_dict.items():
            if place in v:
                state = k
                break
        if state == -1 or lang != 'en':
            return False
    except:
        return False
    try:
        #original_content = BeautifulSoup(record['doc']['data']['text'], 'html.parser').text
        original_content = record['doc']['data']['text']
        content = nlp_content(original_content)
        related = 0 if not determine_related(content=content) else 1
    except:
        original_content = ''
        related = 0
    out = dict()
    out['uid'] = uid
    out['content'] = original_content
    out['place'] = place
    out['state'] = state
    out['related'] = related
    return out

'''
load sal.json file. Use Bingguang and Arezoo's code for Assignment 1.
'''
with open(SAL_PATH) as fsal:
    sal_items = ijson.items(fsal, '')
    state_dict = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
    for item in sal_items:
        for k, v in item.items():
            state_dict[v['ste']].append(k)



# write processed data into preprocessed.json
#output_path = 'preprocessed.json'

try:
    os.remove(output_path)
except:
    pass



out = open(output_path, 'a')
out.write('[')
count = 1

with ZipFile(INPUT_PATH, 'r') as zip:
    with zip.open(zip.namelist()[0]) as f:
        items = ijson.items(f, 'rows.item')
        for record in items:
            record = convert_record(record)
            if record != False:
                js_out = json.dumps(record)
                if count != 1:
                    out.write(', \n')
                out.write(js_out)
                count += 1
                if count % 10000 == 0:
                    print(count, 'has been dealt with')
out.write(']')
out.close()  

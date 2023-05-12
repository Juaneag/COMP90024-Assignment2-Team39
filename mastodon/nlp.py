import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
nltk.download('punkt')
nltk.download('stopwords')

txt = "🔴 Aslef train drivers are striking today and RMT workers have a planned walkout tomorrow - here are the details you need ⤵️ https://www.telegraph.co.uk/business/2023/05/12/train-strikes-today-may-june-2023-dates-aslef-rmt-rail-companies-affected/?utm_medium=Social&utm_campaign=Echobox&utm_source=Twitter#Echobox=1683891338 #press"


out = re.sub(r'https:\/\/[^\s]+', '', txt.lower()) # remove link
out = re.sub(r'[^A-z\s]', ' ', out) # remove all english character words
out = re.sub(r'\s+', ' ', out) # deal with multiple space

tokens = nltk.word_tokenize(out) # tokenisation

# stop words removal
stop_words = set(stopwords.words('english'))
no_stop_words = [w for w in tokens if w not in stop_words]

# Stemming
porterStemmer = PorterStemmer()
stemmed = [porterStemmer.stem(w) for w in no_stop_words]

print(stemmed)

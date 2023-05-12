FROM python:latest

WORKDIR /usr/src/app
EXPOSE 5984

RUN pip install CouchDB2
RUN pip install uuid
RUN pip3 install Mastodon.py
RUN pip install beautifulsoup4
RUN pip install nltk
RUN pip install regex

COPY MastodonStream.py ./

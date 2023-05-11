FROM python:3.11

WORKDIR /usr/src/app

RUN pip install ijson
RUN pip install simplejson

VOLUME ./data

COPY preprocess.py ./preprocess.py

CMD [ "python3", "./pipeline.py" ]
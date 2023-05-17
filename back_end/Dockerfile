FROM python:3.6

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /back_end

COPY configs configs
COPY requirements.txt .
COPY config.py .
COPY run.py .
COPY app app
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["gunicorn", "--log-level", "INFO", "-b", ":8296", "-t", "120", "run:APP"]
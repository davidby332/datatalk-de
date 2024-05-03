FROM python:3.10

RUN apt-get install wget

COPY requirements.txt requirements.txt  

RUN pip install -r requirements.txt

WORKDIR /app

COPY ingest.sh ingest.sh
COPY data_ingestion.py data_ingestion.py
COPY data data

ENTRYPOINT ["sh", "ingest.sh"]
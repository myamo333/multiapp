FROM python:3.9.19-slim

WORKDIR /home/test/webapp

COPY requirements.txt .

RUN apt-get update && apt-get -y upgrade && apt-get -y install git && pip install -r requirements.txt

EXPOSE 8501

COPY . .
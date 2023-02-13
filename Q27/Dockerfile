FROM python:3.9-slim-buster as builder

WORKDIR /code

RUN apt update &&\
    apt install -y gcc &&\
    pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000

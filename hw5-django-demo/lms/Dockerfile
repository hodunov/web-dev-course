FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

ADD . /app/

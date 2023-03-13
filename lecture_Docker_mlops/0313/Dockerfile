FROM python:3.9

ENV PYTHOUNBUFFERED

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get clean
RUN apt-get autoremove -y

WORKDIR /app/mlflow-docker

RUN python -m pip install --upgrade pip setuptools

ADD requirements.txt /app/mlflow-docker/

RUN pip install -r /app/mlflow-docker/requirements.txt
FROM python:3.9
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
WORKDIR /data/app
COPY requirements1.txt /data/app
COPY model.py /data/app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements1.txt
CMD python model.py

FROM python:3.9

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3-pip

WORKDIR /app/project-engineer
COPY ../requirements.txt /app/project-engineer
RUN pip install -r /app/project-engineer/requirements.txt

ENTRYPOINT ["jupyter", "notebook"]
CMD ["--ip", "0.0.0.0", "--port", "8899:8899", "--allow-root", "--NotebookApp.token='eng12345'"]

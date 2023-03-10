FROM python:3.9

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3-pip

WORKDIR /app/project-ds
COPY ../requirements.txt /app/project-ds
RUN pip install -r /app/project-ds/requirements.txt

ENTRYPOINT ["jupyter", "notebook"]
CMD ["--ip", "0.0.0.0", "--port", "8890:8890", "--allow-root", "--NotebookApp.token='ds12345'"]

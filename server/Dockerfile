FROM alpine:latest
FROM python:3.6

WORKDIR  /app

COPY ./HttpServer.py /app
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT uwsgi --socket 0.0.0.0:8080 --protocol=http -w HttpServer:app

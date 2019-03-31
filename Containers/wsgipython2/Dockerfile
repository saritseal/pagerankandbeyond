FROM alpine:latest
FROM python:3.6

WORKDIR  /app

COPY ../server/HttpServer.py /app
COPY ./requirements.txt .

RUN pip3 install -r ../server/requirements.txt

EXPOSE 8081

ENTRYPOINT wsgi --socket 0.0.0.0:8081 --protocol=http -w HttpServer:app &

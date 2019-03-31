FROM alpine:latest
FROM python:3.6


WORKDIR  /app

ADD ../server/HttpServer.py /app
ADD ../server/requirements.txt .

RUN pip3 install -r ../server/requirements.txt

EXPOSE 8080

ENTRYPOINT wsgi --socket 0.0.0.0:8080 --protocol=http -w HttpServer:app &

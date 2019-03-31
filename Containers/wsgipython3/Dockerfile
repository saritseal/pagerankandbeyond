FROM alpine:latest
FROM python:3.6

WORKDIR  /app

COPY ../server/HttpServer.py /app
COPY ./requirements.txt .

RUN pip3 install -r ../server/requirements.txt

EXPOSE 8082

ENTRYPOINT wsgi --socket 0.0.0.0:8082 --protocol=http -w HttpServer:app &

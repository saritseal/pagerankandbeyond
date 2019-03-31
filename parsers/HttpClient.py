import http.client as cl
import hashlib
import requests
from pymonad import List

class HttpContent:
    def __init__(self, content):
        self.content = content
        self.key = hashlib.sha1(self.contruct_url().encode()).hexdigest()


class Content:
    raw_content = []

    def __init__(self, host, port=80, protocol="http", path="/"):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.path = path
        self.key = hashlib.sha1(self.contruct_url().encode()).hexdigest()

    def contruct_url(self):


        if self.path != "/":
            return "{0}:{1}/{2}".format(self.host, self.port, self.path)
        else:
            return "{0}:{1}".format(self.host, self.port)

    def connect_to_url_and_stream(self):
        http_conn = requests.get(self.contruct_url())
        # stream = http_conn.request(method=http_domain.protocol, url=http_domain.contruct_url())
        print(type(stream))
        # [print(x) for x in ]


if __name__ == "__main__" :
    http = Content("www.google.com")
    print(http.key)
    # load_http_stream(http)
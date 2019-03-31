import requests
from typing import List


def parse_links(html_line:str) -> List[str]:

    def get_link_from_line():
        link = ""
        return link

    def return_isunvisited(link:str) -> str:
        return link

    def mutate_ifNotNone(array, value) -> None:
        pass

    link_array = List[str]

    mutate_ifNotNone(link_array, return_isunvisited(get_link_from_line()))

    return link_array

def process_http_stream(url):

    print("Parsing HTTP Stream {url}".format(url=url))
    link_arrays = [parse_links(line) for line in requests.get(url).iter_lines()]

    return link_arrays
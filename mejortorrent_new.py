import re
import urllib.parse
from datetime import datetime
from html.parser import HTMLParser

from novaprinter import prettyPrinter
from helpers import download_file, retrieve_url

class mejortorrent (object):
    url = 'https://www28.mejortorrent.eu'
    name = 'MejorTorrent'
    supported_categories = {
        'all': '0', 
        'movies': 'pelicula', 
        'tv': 'serie'
    }

    def __init__(self):
        pass


def main(query):
    search_url = mejortorrent.url + '/busqueda?q=' + query
    print(search_url)
    print(retrieve_url(search_url))

main('spiderman')
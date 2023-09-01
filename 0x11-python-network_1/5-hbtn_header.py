#!/usr/bin/python3
"""
script that sends a request to the URL and displays the value of the variable 
"""
import requests
from sys import argv


def main(argv):
    url = argv[1]
    r = requests.get(url)
    headers = r.headers.get('X-Request-Id')
    print(headers)

if __name__ == "__main__":
    main(argv)

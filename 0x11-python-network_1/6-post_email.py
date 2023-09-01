#!/usr/bin/python3
"""
Sends a POST request to URL as a parameter and displays the body of the response
"""
import requests
from sys import argv


def main(argv):
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    main(argv)

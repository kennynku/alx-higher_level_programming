#!/usr/bin/python3
"""
takes in URL and requests URL, displays body of response
"""
import urllib.request
from sys import argv

def main(argv):
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)

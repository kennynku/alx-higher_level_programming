#!/usr/bin/python3
"""
script that sends a request to the URL and displays the value of the variable 
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))

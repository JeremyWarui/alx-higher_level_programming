#!/usr/bin/python3
"""
script that sends request to url and
displays 'X-Request-Id'
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with requests.get(url) as res:
            print(res.headers['X-Request-Id'])
    except:
        pass

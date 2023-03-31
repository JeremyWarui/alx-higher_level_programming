#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: ", e.code)    

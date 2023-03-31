#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url).status_code
    if res >= 400:
        print("Error code: {}".format(res))
    else:
        print(res.text)

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
    res = requests.get(url)
    status_cd = res.status_code
    if status_cd >= 400:
        print("Error code: {}".format(status_cd))
    else:
        print(res.text)

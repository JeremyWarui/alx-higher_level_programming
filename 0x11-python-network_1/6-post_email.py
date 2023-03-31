#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
using 'requests'
"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    url = argv[1]
    with requests.post(url, data=email) as res:
        print(res.text)

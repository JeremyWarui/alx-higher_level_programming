#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urlencode(email)
    data = data.encode("ascii")
    req = Request(argv[1], data)
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))

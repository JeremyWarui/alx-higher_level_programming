#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as res:
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t-content: {}".format(res))
        print("\t-utf8 content: {}".format(res.decode('utf-8')))

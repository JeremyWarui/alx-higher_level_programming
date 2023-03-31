#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        response = res.read()
        print(
        """Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(response),
                                 response, response.decode('utf-8')))

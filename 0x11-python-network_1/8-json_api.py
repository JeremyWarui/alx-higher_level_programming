#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    data = {'q': "" if len(argv) < 2 else argv[1]}

    try:
        req = requests.post(url, data)
        dict = req.json()
        if dict:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")

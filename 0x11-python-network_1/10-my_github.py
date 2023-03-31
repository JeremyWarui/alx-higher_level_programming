#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
You must use Basic Authentication with a
personal access token as password to access
to your information (only read:user permission is needed)
"""
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    data = auth.HTTPBasicAuth(user, passwd)
    url = "https://api.github.com/user"
    req = get(url, auth=data)
    print(req.json().get('id'))

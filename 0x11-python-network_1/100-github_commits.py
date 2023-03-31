#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository by the user
script takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    try:
        repo = argv[1]
        owner = argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repo)
        req = get(url)
        commits = req.json()
        for i in range(0, 10):
            print("{}: {}".format(commits[i].get('sha'),
                                  commits[i]
                                  .get('commit')
                                  .get('author')
                                  .get('name')))
    except Exception as e:
        pass

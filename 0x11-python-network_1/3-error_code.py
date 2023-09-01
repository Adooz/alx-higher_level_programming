#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
 
#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
"""
from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

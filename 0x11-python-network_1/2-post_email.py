#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
"""
from sys import argv
from urllib import parse
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('ascii')
    request = request.Request(url, data=data)
    with request.urlopen() as response:
        body = response.read().decode('utf-8')
        print(body)
#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
"""
from sys import argv
from urllib import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    with requests.post(url, data=data) as response:
        if response.status == 200:
            print(f"Your email is: {email}")
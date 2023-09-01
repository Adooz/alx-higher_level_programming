#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status using requests"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
    
if response.status_code == 200:
    # If the request was successful, you can access the content of the response
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content.decode(utf-8)}")
else:
    print("Error:")
    print(f"\t- status code: {response.status_code}")

#!/usr/bin/python3
"""takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a
parameter. The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and
not empty, display the id and name like 
this: [<id>] <name> Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    if r.status_code == 200:
        if r.text != "":
            try:
                data = r.json()
                print("[{}] {}".format(data.get("id"), data.get("name")))
            except ValueError:
                print("Not a valid JSON")
        else:
            print("No result")
    else:
        print("Error: {}".format(r.status_code))

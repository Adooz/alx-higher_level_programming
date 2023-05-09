#!/usr/bin/python3
def uppercase(var):
    new = ""
    for char in var:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print()

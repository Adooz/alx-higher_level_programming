#!/usr/bin/python3
for value in range(100):
    if value == 99:
        print("{:02d}".format(value), end="\n")
    else:
        print("{:02d},".format(value), end=" ")

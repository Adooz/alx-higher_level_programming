#!/usr/bin/python3
for value in range(10):
    for num in range(10):
        if value < num:
            if value == 8 and num == 9:
                print("{:d}{:d}".format(value, num), end="\n")
            else:
                print("{:d}{:d},".format(value, num), end=" ")

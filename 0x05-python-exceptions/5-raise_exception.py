#!/usr/bin/python3
def raise_exception():
    try:
        2 + "Alpha"
    except(TypeError):
        raise TypeError

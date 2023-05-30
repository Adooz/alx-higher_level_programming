#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        le(message)
    except(NameError):
        raise NameError(f"{message}")

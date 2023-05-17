#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(list(set(my_list)))


"""
def uniq_add(my_list=[]):
    from functools import reduce
    return reduce(lambda x, y: x + y, set(my_list))
"""

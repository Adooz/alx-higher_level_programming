#!/usr/bin/python3
def search_replace(my_list, search, replace):
    output_list = [value if value != search else replace for value in my_list]
    return output_list

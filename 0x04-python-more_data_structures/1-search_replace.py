#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [elem if elem != search else replace for elem in my_list]
    return new

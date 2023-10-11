#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_items = sorted(a_dictionary)
    for item in sort_items:
        print("{}: {}".format(item, a_dictionary[item]))

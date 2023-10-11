#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = {}
    for key in a_dictionary:
        mul_dict[key] = a_dictionary[key] * 2
    return mul_dict

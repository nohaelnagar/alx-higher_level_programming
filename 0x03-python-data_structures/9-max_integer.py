#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)

    maxi = my_list[0]
    for int in my_list:
        if my_list[int] > maxi:
            maxi = my_list[int]
    return (maxi)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least two elements, filling in with 0s if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    
    # Create a new tuple with the sums of the first two elements of the input tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result

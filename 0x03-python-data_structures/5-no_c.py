def no_c(my_string):
    new_string = ''
    for letter in my_string:
        if letter != 'c' or letter != 'C':
            new_string += letter
    return new_string

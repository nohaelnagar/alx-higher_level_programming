#!/usr/bin/python3
""" Empty Square class """


class Square:
    """ class Square that defines a squar """

    def __init__(self, size=0):
        """
            size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate and return the area of the square """
        return self.__size ** 2

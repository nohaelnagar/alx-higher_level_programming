#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range (len(matrix)):
        for y in range (len(matrix[x])):
            print("{:d}".format(matrix[x][y]), end="")
            if y != (len(matrix[x]) - 1):
                print(" ", end="")
        print("")

print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i in row:
                print("{:d}".format(i), end=" " if i != row[-1]) else "")
            print()

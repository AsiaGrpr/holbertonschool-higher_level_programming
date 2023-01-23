#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        print('\n'.join(' '.join('{:d}'.format(i)
                                 for i in x) for x in matrix))

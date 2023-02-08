#!/usr/bin/python3
'''module where I had to write a function to know if an
object is an instance of a specified class'''


def is_same_class(obj, a_class):
    '''function that returns True if the object is exactly
    an instance of the specified class ; otherwise False'''

    return (type(obj) == a_class)

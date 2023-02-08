#!/usr/bin/python3
'''module to define if he object is an instance of a class or
inherited class'''


def is_kind_of_class(obj, a_class):
    ''' function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from,
    the specified class ; otherwise False'''

    return (isinstance(obj, a_class))

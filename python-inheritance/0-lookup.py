#!/usr/bin/python3
'''module to print list of attribute of an object'''


def lookup(obj):
    '''function that returns the list of
    available attributes and methods of an object'''

    return(dir(obj))

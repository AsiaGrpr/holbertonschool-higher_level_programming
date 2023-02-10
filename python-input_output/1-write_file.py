#!/usr/bin/python3
'''module with function to write a file'''


def write_file(filename="", text=""):
    '''
    Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    '''

    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)

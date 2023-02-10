#!/usr/bin/python3
'''module with function to append text in a file'''


def append_write(filename="", text=""):
    '''
    Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    '''

    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)

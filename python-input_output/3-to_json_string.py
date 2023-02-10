#!/usr/bin/python3
import json
'''module to return JSON representation'''


def to_json_string(my_obj):
    """
    Write a function that reads a text file (UTF8) and prints it to stdout
    """

    return json.dumps(my_obj)

#!/usr/bin/python3
'''module to Write a script that adds all arguments
to a Python list, and then save them to a file'''
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    save(load("add_item.json") + sys.argv[1:], "add_item.json")
except:
    save(sys.argv[1:], "add_item.json")

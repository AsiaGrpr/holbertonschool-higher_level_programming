#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx < 0 or idx >= len(my_list):
            return(my_list.copy())
        else:
            a = my_list.copy()
            a[idx] = element
            return(a)

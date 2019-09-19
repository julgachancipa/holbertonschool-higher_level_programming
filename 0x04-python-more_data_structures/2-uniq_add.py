#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_list = set(my_list)
    add_list = list(add_list)
    res = 0
    for i in range(len(add_list)):
        res += add_list[i]
    return res

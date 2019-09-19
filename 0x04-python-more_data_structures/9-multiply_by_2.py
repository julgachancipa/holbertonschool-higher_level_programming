#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dic = {}
    for key, val in a_dictionary.items():
        nw_dic[key] = val * 2
    return nw_dic

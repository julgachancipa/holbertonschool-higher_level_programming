#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_key, best_val = "", 0;
    for key, val in a_dictionary.items():
        if val > best_val:
            best_val = val
            best_key = key
    return key

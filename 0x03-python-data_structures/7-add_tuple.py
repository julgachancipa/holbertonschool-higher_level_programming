#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        a_x = 0
    else:
        a_x = tuple_a[0]
    if len(tuple_a) < 2:
        a_y = 0
    else:
        a_y = tuple_a[1]
    if len(tuple_b) < 1:
        b_x = 0
    else:
        b_x = tuple_b[0]
    if len(tuple_b) < 2:
        b_y = 0
    else:
        b_y = tuple_b[1]
    a = a_x + b_x
    b = a_y + b_y
    tuple_c = (a, b)
    return tuple_c

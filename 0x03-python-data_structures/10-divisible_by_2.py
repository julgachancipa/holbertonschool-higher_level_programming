#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            nw[i] = True
        else:
            nw[i] = False
    return nw

#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    dividendo = 0
    divisor = 0
    for i in range(len(my_list)):
        dividendo += my_list[i][0] * my_list[i][1]
        divisor += my_list[i][1]
    return dividendo / divisor

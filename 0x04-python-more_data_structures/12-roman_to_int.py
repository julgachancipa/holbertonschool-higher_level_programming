#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or None:
        return 0
    last = 1
    res = 0
    for i in range(len(roman_string) - 1, -1, -1):
        n = conv_rom_int(roman_string[i])
        if last == -1:
            break
        if n == last:
            res += n
        elif n > last:
            last = last_fun(last)
            res += n
        elif n < last:
            last = last_fun(last)
            res -= n
    return res


def conv_rom_int(n):
    trl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return trl[n]


def last_fun(last):
    l = {1: 5, 5: 10, 10: 50, 50: 100, 100: 500, 500: 1000, 1000: -1}
    return l[last]

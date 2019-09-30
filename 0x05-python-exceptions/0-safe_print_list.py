#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for n in range(0, x):
            print("{}".format(my_list[n]), end='')
            num += 1
    except IndexError:
        pass
    finally:
        print('')
        return num

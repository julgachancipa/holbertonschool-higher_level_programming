#!/usr/bin/python3
def pascal_triangle(n):
    """
    hat returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    big_list = []
    if n > 0:
        big_list.append([1])
        for count in range(0, n - 1):
            i = -1
            mini_list = []
            while i < len(big_list[count]) - 1:
                if i == -1:
                    mini_list.append(1)
                else:
                    mini_list.append(big_list[count][i] +
                                     big_list[count][i + 1])
                i += 1
            mini_list.append(1)
            big_list.append(mini_list)
    return big_list

#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        lineNum = 0
        for line in myFile:
            lineNum += 1
            print(line, end='')
            if lineNum == nb_lines:
                break
    return lineNum

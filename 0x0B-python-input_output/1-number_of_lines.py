#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    returns the number of lines of a text file
    """
    with open(filename, encoding="utf-8") as myFile:
        lineNum = 0
        for line in myFile:
            lineNum += 1
    return lineNum

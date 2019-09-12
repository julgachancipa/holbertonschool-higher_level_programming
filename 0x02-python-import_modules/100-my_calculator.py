#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import exit
    from sys import argv
    l = len(argv)
    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
    elif argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
    elif argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
    elif argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)

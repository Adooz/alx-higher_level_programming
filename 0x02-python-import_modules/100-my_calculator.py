#!/usr/bin/python3
"""
if __name__ == "__main__":
    from sys import argv

    op = ["+", "-", '*', "/"]

    if len(argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in op:
        print("Unknown operator. Available opertors: +, -, * and /")
        exit(1)
    else:
        from calculator_1 import add, sub, mul, div

        value1 = int(argv[1])
        value2 = int(argv[3])

        if argv[2] == op[0]:
            result = int(add(value1, value2))
        elif argv[2] == op[1]:
            result = int(sub(value1, value2))
        elif argv[2] == op[2]:
            result = int(mul(value1, value2))
        elif argv[2] == op[3]:
            result = int(div(value1, value2))
        print("{:d} {} {:d} = {:d}".format(value1, argv[2], value2, result))
"""

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = ['+', '-', '*', '/']

        if argv[2] == op[0]:
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif argv[2] == op[1]:
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif argv[2] == op[2]:
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        elif argv[2] == op[3]:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

        elif argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

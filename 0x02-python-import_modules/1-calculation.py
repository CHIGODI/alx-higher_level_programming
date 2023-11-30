#!/usr/bin/python3
import calculator_1 as cal


def calculator():
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cal.add(a,b)))
    print("{:d} - {:d} = {:d}".format(a, b, cal.sub(a,b)))
    print("{:d} * {:d} = {:d}".format(a, b, cal.mul(a,b)))
    print("{:d} / {:d} = {:d}".format(a, b, cal.mul(a,b)))


if __name__ == "__main__":
    calculator()

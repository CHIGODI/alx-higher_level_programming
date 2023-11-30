#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

argument = sys.argv
operators = {'+', '-', '*', '/'}

def calculator():
    if len(argument) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = argument[2]
        if operator not in operators:
            print(f"Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        a = int(argument[1])
        b = int(argument[3])

        if operator == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif operator == "-":
            print(f"{a} - {b} = {sub(a, b)}")
        elif operator == "*":
            print(f"{a} * {b} = {mul(a, b)}")
        elif operator == "/":
            print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    calculator()

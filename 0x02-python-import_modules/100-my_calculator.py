#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

argument = sys.argv
operator = argument[2]
sum_args = add(int(argument[1]), int(argument[3]))
sub_args = sub(int(argument[1]), int(argument[3]))
mul_args = mul(int(argument[1]), int(argument[3]))
div_args = div(int(argument[1]), int(argument[3]))

def calculator():
    if len(argument) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if operator == '+':
            print(f"{argument[1]} + {argument[3]} = {sum_args}")
        elif operator == '-':
            print(f"{argument[1]} - {argument[3]} = {sub_args}")
        elif operator == '*':
            print(f"{argument[1]} * {argument[3]} = {mul_args}")
        elif operator == '/':
            print(f"{argument[1]} / {argument[3]} = {div_args}")
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

if __name__ == "__main__":
    calculator()

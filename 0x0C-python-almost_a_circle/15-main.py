#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    Rectangle.save_to_file(None)

    with open("Rectangle.json", "r") as file:
        print(file.read())

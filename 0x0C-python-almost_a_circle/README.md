# Project Title: 0x0C Python - Almost a Circle

## Overview
This project is part of the Higher-level curriculum in the AirBnB clone series. It focuses on reviewing various aspects of Python programming, including object-oriented programming (OOP), unit testing, exception handling, file I/O, and more. The primary goal is to prepare you for the upcoming challenges in the AirBnB project.

## Tasks
### Task 0: If it's not tested it doesn't work
- Ensure all files, classes, and methods are unit tested and PEP 8 validated.

### Task 1: Base class
- Create a folder named `models` with an empty file `__init__.py` inside, making it a Python package.
- Create a file named `models/base.py` with a class named `Base` that includes necessary features.

### Task 2: First Rectangle
- Write a class `Rectangle` that inherits from `Base` and includes private instance attributes with getters and setters.

### Task 3: Validate attributes
- Add validation of all setter methods in the `Rectangle` class.

### Task 4: Area first
- Add a method `def area(self):` to the `Rectangle` class that returns the area of the rectangle.

### Task 5: Display #0
- Add a method `def display(self):` to the `Rectangle` class that prints the rectangle using the `#` character.

### Task 6: __str__
- Override the `__str__` method in the `Rectangle` class to return a custom string representation.

### Task 7: Display #1
- Modify the `Rectangle` class to allow users to change the character used for drawing by providing an optional argument to the `display` method.

### Task 8: Update #0
- Update the `Rectangle` class to add a method `def update(self, *args):` that assigns arguments to each attribute.

### Task 9: Update #1
- Update the `Rectangle` class to add a method `def update(self, *args, **kwargs):` that assigns arguments to each attribute and handles key/value pairs.

### Task 10: And now, the Square!
- Create a file named `models/square.py` with a class named `Square` that inherits from `Rectangle`.

### Task 11: Square size
- Update the `Square` class to include a constructor that calls the constructor of the `Rectangle` class.

### Task 12: Square update
- Update the `Square` class to add a method `def update(self, *args, **kwargs):` that assigns arguments to each attribute and handles key/value pairs.

### Task 13: Rectangle instance to dictionary representation
- Add a method `def to_dictionary(self):` to the `Rectangle` class that returns the dictionary representation of a rectangle.

### Task 14: Square instance to dictionary representation
- Add a method `def to_dictionary(self):` to the `Square` class that returns the dictionary representation of a square.

### Task 15: Dictionary to JSON string
- Add a class method `def to_json_string(cls, list_dictionaries):` to the `Base` class that returns the JSON string representation of a list of dictionaries.

### Task 16: JSON string to file
- Add a class method `def save_to_file(cls, list_objs):` to the `Base` class that writes the JSON string representation of a list of objects to a file.

### Task 17: JSON string to dictionary
- Add a class method `def from_json_string(cls, json_string):` to the `Base` class that returns the list of the JSON string representation `json_string`.

### Task 18: Dictionary to Instance
- Add a class method `def create(cls, **dictionary):` to the `Base` class that returns an instance with all attributes already set.

### Task 19: File to instances
- Update the `Base` class with a class method `def load_from_file(cls):` that returns a list of instances.

## Usage
Execute the following command to run the tests:
```bash
python3 -m unittest discover tests

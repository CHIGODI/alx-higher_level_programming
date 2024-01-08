#!/usr/bin/python3
"""
   module defining a class MyList
"""

class MyList(list):
    """
    Inherits from list and prints the list but sorted
    """
    def print_sorted(self):
        if all(isinstance(value, int) for value in self):
            sorted_list = self[:]
            sorted_list.sort()
            print(sorted_list)
        else:
            return None

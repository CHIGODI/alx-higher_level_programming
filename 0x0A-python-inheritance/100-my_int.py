#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    def __eq__(self, other):
        """
        __eq__ is the equal method here iam swaping it with other
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        __eq__ is the equal method here iam swaping it with other
        """
        return super().__eq__(other)

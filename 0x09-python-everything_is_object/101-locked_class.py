#!/usr/bin/python3
""" This class is locked for firstname only! """


class LockedClass:
    """ only first name instance attribute allowed """
    __slots__ = ('first_name', )

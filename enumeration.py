"""Module for Enumeration"""

from enum import Enum

def enumer():
    """Function for enumeration."""

    class Color(Enum):
        red = 1
        blue = 2
        green = 3
        pink = 234
        orange = 26
        black = 3000
        peach = 19

    print(Color.red)
    print(Color['red'])
    print(Color(1))
    print()
    print([x for x in Color])
    print()

enumer()

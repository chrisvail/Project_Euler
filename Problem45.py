from Problem44 import ispent
from math import sqrt
from itertools import count


def ishex(n):
    """
    Checks if a given n is a hexagonal number
    """
    if (sqrt((8 * n) + 1) + 1 )/ 4 % 1 == 0:
        return True
    else:
        return False

i = 0
# Loops through numbers until break condition is met
for n in count(286):

    # Creates a triangle number
    i = (n * (n + 1)) / 2

    # If triangle number is a pentagonal number
    # and a hexagonal number its printed
    if ispent(i) and ishex(i):
        print(i)
        break
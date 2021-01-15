from math import sqrt, gcd
from itertools import count
from fractions import Fraction

def main():

    target = 1000000000
    total = 0
    fundx, fundy = 2, 1
    x, y = 7, 4
    a = 0

    while True:
        b = 0
        if ((2*x + 1) / 3) % 1 == 0:
            a = (2*x + 1) / 3
            b = 1

        else:
            a = (2*x - 1) / 3 
            b = -1

        area = 0.5 * (a + b) * sqrt( (a ** 2) - (((a + b) /2) ** 2))
        assert area % 1 == 0
        #if area % 1 != 0:
        #    area = 0.5 * (a - 1) * sqrt( (a ** 2) - (((a - 1) /2) ** 2))
        if 3 * a + b < target:
            total += 3 * a + b

        else:
            break
        print(a, area)
        x, y = x * fundx + 3 * y * fundy, fundx * y + fundy * x

    print(total)
    
if __name__ == '__main__':
    main()
from math import sqrt
from itertools import count
from StandardFunctions import squares_less_than
from fractions import Fraction

def main():
    squares = [_ for _ in squares_less_than(1001)]
    solutions = [0 for _ in range(1001)]

    for i in range(1, 1001):
        if i in squares:
            continue

        for frac in yield_fractions(continued_fraction(i)):

            x = frac.numerator
            y = frac.denominator

            if (x*x) - (i * y * y) == 1:
                solutions[i] = x
                print([i,x])
                break

    print(max(solutions))
    print(solutions.index(max(solutions)))


def yield_fractions(period):

    for i in count():
        frac = Fraction(0)
        for j in range(i):
            frac = Fraction(1, period[1][j % len(period[1])] + frac)

        
        yield period[0] + frac

def continued_fraction(x):
    """
    Calculates the continued fraction for the square root of x
    """

    period = [0, []]
    for i in range(x + 1):
        if i * i > x:
            period[0] = i - 1
            break

    numerator = period[0]
    n = period[0]
    denominator = 1

    while True:

        if denominator == 1 and len(period[1]) > 0:
            break

        n = (denominator / (sqrt(x) - numerator)) // 1

        denominator = (x - (numerator * numerator)) // denominator
        
        numerator = abs(numerator - (denominator * n))

        period[1].append(int(n))

    return period


            

if __name__ == '__main__':
    main()
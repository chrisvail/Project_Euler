from time import clock
from fractions import Fraction as f

def main():
    a = recurse(0, 1, f(1), 0)
    prize = (1 - a) / a
    prize = int(prize + 1)
    print(prize)

def recurse(blue, red, prob, depth):
    
    if depth == 15:
        return prob if blue > 7 else 0

    else:
        pWin = 0
        pWin += recurse(blue + 1, red + 1, f(1, red + 1) * prob, depth + 1)
        pWin += recurse(blue, red + 1, f(red, red + 1) * prob, depth + 1)
        return pWin

if __name__ == '__main__':
    main()
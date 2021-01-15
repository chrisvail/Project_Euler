from math import sqrt
from decimal import Decimal, getcontext


def main():
    
    getcontext().prec = 110

    squares = [i * i for i in range(11)]
    total = 0

    for i in range(1, 100):
        if i in squares:
            continue

        root = str(Decimal(i).sqrt())

        total += sum([int(x) for x in root[2:101]])
        total += int(root[0])

    print(total)
       

if __name__ == '__main__':
    main()
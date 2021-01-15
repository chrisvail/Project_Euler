from time import clock
from math import sqrt
from StandardFunctions import is_palindrome


def main():
    t0 = clock()

    target = 10 ** 8
    total = 0

    for a in gen_square_sum(target):
        if a == 1:
            continue
        if is_palindrome(str(a)):
            total += a

    print(total)
    t1 = clock()
    print("Time: {}".format(t1 - t0))

def gen_square_sum(max):

    max_range = int(sqrt(max)) + 1
    numbers = set()

    for start in range(1, max_range):

        total = start * start
        for addition in range(start + 1, max_range):
            
            total += (addition * addition)
            if total > max:
                break
                
            numbers.add(total)

    return sorted(list(numbers))


if __name__ == '__main__':
    main()
from itertools import count
from time import clock as time


def main():

    t0 = time()

    counter = 0
    for n in generate_powerful(100):

        if test(n):
            counter += 1
            
            if counter == 30:
                print(n)
                break

    t1 = time()
    print("Solution took {} seconds".format(t1 - t0))

def generate_powerful(n):

    numbers = []

    for i in range(n):
        for j in range(n):
            number = i ** j

            if number >= 2 ** (n + 1):
                break
            else:
                numbers.append(number)

    numbers = sorted(list(set(numbers)))
    for i in numbers:
        yield i

def test(n):
    x = n
    digits = []

    while x != 0:
        digits.append(x % 10)
        x = x // 10

    power = 1
    total = sum(digits)

    if total == 1:
        return False

    while total < n:
        
        total = sum(digits) ** power

        if total == n:
            return True
        else:
            power += 1

    return False


if __name__ == '__main__':
    main()
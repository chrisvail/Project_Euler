from Problem27 import primes as genprimes
from itertools import count

# Generates a reasonably large number of primes
PRIMES = [n for n in genprimes(1000000)]

def squares_less_than(n):
    """
    Yields square numbers below n
    """
    i = 1
    while i * i <= n:
        yield i * i
        i += 1


def broken_conjecture(n):
    """
    Returns true if Goldbachs other conjecture is broken
    """
    for i in squares_less_than(n / 2):
        if (n - (2 * i)) in PRIMES:
            return False

    return True


def main():
    
    # Loops through odd numbers above 9
    for i in count(start=9, step=2):
        # Discards prime numbers
        if i in PRIMES:
            continue
    
        else:
            # If conjecture broken then returns counter example
            if broken_conjecture(i):
                return "Conjecture broken by: {}".format(i)


# Runs program only if its run as a script
if __name__ == '__main__':
    print(main())
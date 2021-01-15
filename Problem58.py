from fractions import Fraction
from itertools import count

def diagonal_percentage():
    """
    Yields progressive diagonal prime percentages for an Ulam spiral
    """
    # Sets numerator to 0 prime found
    num = 0

    # Loops through integers infinitely
    for i in count(1):
        # Tests if diagonals are prime and adds to numerator if it is
        if is_prime(4*(i ** 2) + 1):
            num += 1
        
        if is_prime(4*(i ** 2) - 2 * i + 1):
            num += 1
        
        if is_prime(4*(i ** 2) + 2 * i + 1):
            num += 1

        # One diagonal is square numbers so cant be prime

        # Returns percentage as a fraction to avoid imprecision
        yield (Fraction(num, (4 * i) + 1), i)


def _try_composite(a, d, n, s):
    """
    Returns true if value is definitely composite using miller rabin test
    """
    if pow(a, d, n) == 1:
        return False

    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False

    return True # n  is definitely composite

 
def is_prime(n, _precision_for_huge_n=16):
    
    # Tests for known prime divisors
    if n in _known_primes or n in (0, 1):
        return True

    if any((n % p) == 0 for p in _known_primes):
        return False

    # Runs miller rabin primality test using known non lying witnesses

    d, s = n - 1, 0

    while not d % 2:

        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))

    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))

    if n < 118670087467: 
        if n == 3215031751: 
            return False

        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))

    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))

    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))

    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s)
                       for a in (2, 3, 5, 7, 11, 13, 17))

    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def main():

    # Tests percentage of diagonals are prime until condition reached
    for i in diagonal_percentage():
        
        if i[0] < Fraction(1, 10):
            # Prints out answer
            print((i[1] * 2) + 1)
            break
        

# Runs main only if program run as script
if __name__ == "__main__":
    main()
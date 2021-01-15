from Problem27 import primes as genprimes
from Problem58 import is_prime
from itertools import combinations, permutations

# Generates list of primes not including 2
p = genprimes(10000)
next(p)
primes = [x for x in p]

def concatprimes(plist):
    """
    Checks if 2 primes can be concatenated in any way and be prime
    """
    for x, y in permutations(plist, 2):
        
        if (int(''.join([str(x), str(y)]))) in primes \
            or is_prime(int(''.join([str(x), str(y)]))):
            continue
        else:
            return False

    # Returns true if it can be concatenated in either way
    return True


def main():

    # Creates a list of concatenatable pairs
    concatenatable_pairs = []

    # Loops through all combinations of 2 primes and populates concatenatable primes
    for plist in combinations(primes, 2):
        
        if concatprimes(plist):
            concatenatable_pairs.append(plist)

    # Loops through all concatentatable pairs
    for a, b in concatenatable_pairs:
        for c in primes:
            # Checks if c is also concatenatable
            if c < b:
                continue

            elif all( x in concatenatable_pairs for x in [(a, c), (b, c)]):
                for d in primes:
                    # Checks if d is also concatenatable
                    if d < c:
                        continue

                    elif all(y in concatenatable_pairs for y in [(a, d), (b, d), (c, d)]):
                        for e in primes:
                            # Checks if e is also concatenatable
                            if e < d:
                                continue

                            elif all(z in concatenatable_pairs for z in [(a, e), (b, e), (c, e), (d, e)]):
                                # Prints out answer
                                print("{} {} {} {}".format(a,b,c,d))
                                print(sum([a, b, c, d, e]))
                                return


# Runs main only if program run as script
if __name__ == '__main__':
    main()
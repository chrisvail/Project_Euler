from itertools import count

def quad(a, b):
    """
    Generator function yields successive values of n^2 + an + b
    """
    for i in count(0):
        yield i*i + a*i + b


def primes(primerange):
    """
    Generator function that yields successive primes below primerange
    """
    # Creates a list of boolean values to represent primes
    bits = [False for _ in range(primerange)]
    # 0 and 1 are not prime so are set to true
    bits[0], bits[1] = True, True
    # Loops through bits and sets multiples of primes to True
    for i in range(primerange):
        # Skips composite numbers
        if bits[i]:
            continue
        else:
            # Sets all multiples of the current prime to True
            for j in range(i * 2, primerange, i):
                bits[j] = True

            # Yields the current prime
            yield i


def main():
    # Sets variables
    coefficientB = []
    primeset = set()
    maxvals = (0, 0, 0)
    counter = 0

    # Generates a list of primes below 1000 and a set below 2 million
    for i in primes(200000):
        if i < 1000:
            coefficientB.append(i)
        primeset.add(i)

    # Loops through combinations of a and b
    for a in range(-999, 1000, 1):
        for b in coefficientB:
            # Resets counter for current loop
            counter = 0
            # Goes through successive values of quad until composite is reached
            for i in quad(a, b):
                if i not in primeset:
                    # Finds longest chain
                    if maxvals[0] < counter:
                        maxvals = counter, a, b
                    break
                else:
                    counter += 1

    # Prints answer
    print(maxvals[1] * maxvals[2])
    

if __name__ == '__main__':
    main()
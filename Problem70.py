from StandardFunctions import genprimes
from fractions import Fraction

print("Starting prime list")
primes = genprimes(10000000)
print("Finished prime list")

factors = [[] for _ in range(10000001)]

for i in primes:
    for j in range(i, 10000001, i):
        factors[j].append(i)
print("Completed decomposition")


def main():
    
    minphi = [0, 10000001]

    for i in range(10, 10000001):
        phi_i = phi(i)
        if is_permutation(i, phi_i):
            if i / phi_i < minphi[1]:
                minphi = i, i / phi_i

    print(minphi)
    

def is_permutation(a, b):
    """
    Checks number a is a permutation of b
    """
    
    return sorted(list(str(a))) == sorted(list(str(b)))


def phi(n):

    for j in factors[n]:
        n = n * (1- Fraction(1, j))

    return n.numerator if n.denominator == 1 else n


if __name__ == '__main__':
    main()
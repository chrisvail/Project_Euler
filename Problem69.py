from StandardFunctions import genprimes
from fractions import Fraction

primes = genprimes(1000000)
print("Completed prime list")
factors = [[] for _ in range(1000001)]

for i in primes:
    for j in range(i, 1000001, i):
        factors[j].append(i)
print("Completed decomposition")

def main():

    phi_over_n = [0 for _ in range(1000001)]

    for n in range(2, 1000001):
        phi_over_n[n] = n / phi(n)

        if n % 100000 == 0:
            print("Completed {}".format(n))

    print(max(phi_over_n))
    print(phi_over_n.index(max(phi_over_n)))


def phi(n):

    ''' if n in primes:
        return n - 1 '''

    for j in factors[n]:
        n = n * (1- Fraction(1, j))

    return n.numerator if n.denominator == 1 else n

    
if __name__ == '__main__':
    main()
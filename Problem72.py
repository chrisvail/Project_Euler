from StandardFunctions import genprimes
from fractions import Fraction

number_range = 1000001

primes = genprimes(number_range)
print("Completed prime list")
factors = [[] for _ in range(number_range)]

for i in primes:
    for j in range(i, number_range, i):
        factors[j].append(i)
print("Completed decomposition")

def main():

    phi_values = [phi(x) for x in range(2, number_range)]
    print("Completed phi list")

    print(sum(phi_values))
    # 303963552391


def phi(n):
    """
    Returns the value of eulers phi function for a value n
    """
    ''' if n in primes:
        return n - 1 '''

    for j in factors[n]:
        n = n * (1 - Fraction(1, j))

    return n.numerator if n.denominator == 1 else n


if __name__ == "__main__":
    main()
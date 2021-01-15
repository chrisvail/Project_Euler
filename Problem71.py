from fractions import Fraction
from StandardFunctions import genprimes

''' print("Starting prime list")
primes = genprimes(1000001)
print("Finished prime list")

factors = [[] for _ in range(1000001)]

for i in primes:
    for j in range(i, 1000001, i):
        factors[j].append(i)
print("Completed decomposition")

coprimes = set()

for i in factors:
    for j in factors:
         '''

fraction_list = set()

for j in range(1, 1000001):
    if j % 1000 == 0:
        print(j)
    for i in range( int(j * (3 / 7)) - 1, int(j * (3 / 7)) + 1):
            try:
                fraction_list.add(Fraction(i, j))
            except ZeroDivisionError:
                pass

print("Finished creating list")
fraction_list = list(fraction_list)
print("Made list")
fraction_list = sorted(fraction_list)
print("Sorted list")
print(fraction_list[fraction_list.index(Fraction(3, 7)) - 1])


# 428570/999997
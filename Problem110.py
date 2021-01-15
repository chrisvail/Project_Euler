from StandardFunctions import genprimes
from itertools import combinations_with_replacement

primerange = 40
max_power = 4

primes = genprimes(primerange)[::-1]
numbers = []

counter = 0
for powers in combinations_with_replacement(list(range(max_power)), len(primes)):
    counter += 1

    if counter % 10000 == 0:
        print(counter)

    number = 1
    div_total = 1
    for i in range(len(primes)):
        number *= (primes[i] ** powers[i])
        div_total *= ((2 * powers[i]) + 1) 

    numbers.append((number, (div_total + 1) // 2))

numbers = sorted(numbers, key= lambda x: x[0])

for number, dividers in numbers:

    if dividers > 4000000:
        print(number)
        break
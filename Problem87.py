from itertools import combinations_with_replacement
from StandardFunctions import primes

target = 50000000

numbers = [False for _ in range(target + 1)]

for x in primes(7072):               # int(target ** 0.5) + 2):
    for y in primes(369):            # int(target ** 0.33) + 2):
        for z in primes(85):         # int(target ** 0.25) + 2):
            try:
                numbers[x ** 2 + y ** 3 + z ** 4] = True
            except IndexError:
                pass

print([target, sum(numbers)]) 
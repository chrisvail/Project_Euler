from StandardFunctions import genprimes
from itertools import count

primes = genprimes(1000)

for target in count():
    
    
    ways = [0 for _ in range(target + 1)]
    ways[0] = 1

    for i in primes:
        for j in range(i, target + 1):
            ways[j] += ways[j - i]



    print(ways[-1] - 1)
    if ways[-1] - 1 > 5000:
        print(target)
        break
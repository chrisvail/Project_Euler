from time import clock
from StandardFunctions import genprimes

t0 = clock()

primes = genprimes(500000)
print("Prime gen time: {}".format(clock() - t0))

flag = True

for n, p in enumerate(primes):
    n += 1

    if n % 2 == 0:
        continue

    r = (2 * p * n) % (p * p)

    if r > 10 ** 10:
        t1 = clock()
        print("n = {}\tp = {}\tr = {}".format(n, p, r))
        print("Time: {}".format(t1 - t0))
        break

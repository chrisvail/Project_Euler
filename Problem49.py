from Problem27 import primes
from itertools import permutations, combinations

primeset = set()
permset = set()
skipset = set()

# Creats a set of primes 4 digit primes
for i in primes(10001):
    if i < 1000:
        continue
    elif i > 10000:
        break
    else:
        primeset.add(i)

#
for i in primeset:
    # Clears set of permutations 
    permset.clear()
    # Creates a set of all permutations of i
    permset.add(i)
    string = str(i)
    for perm in permutations(string):
        perm = int("".join(perm))
        permset.add(perm)
    
    # Loops through combinations of permutations intersect with primes
    # and looks for arithmetic sequence 
    for cmbo in combinations(permset & primeset, 3):
        if cmbo[1] - cmbo[0] == cmbo[2] - cmbo[1] and cmbo[0] != 1487:
            # Prints answer
            print("{}{}{}".format(cmbo[0], cmbo[1], cmbo[2]))
            exit(0)

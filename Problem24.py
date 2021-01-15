from itertools import permutations

# Creates empty list for permutations
perm = []

# Populates permutations list
for i in permutations([0,1,2,3,4,5,6,7,8,9]):
    perm.append(i)

# Prints out answer
print(''.join([str(i) for i in perm[999999]]))

"""from math import factorial as fac

target = 1000000
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = []

while len(numbers) != 1:
    for index, value in enumerate(numbers):
        if fac(len(numbers) - 1) * (index + 1) > target:
            perm.append(value)
            target -= fac(len(numbers) - 1) * index
            del numbers[index]

perm.append(numbers[0])

for num in perm:
    print(num, end='')

print()"""
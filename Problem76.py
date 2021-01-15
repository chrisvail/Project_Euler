target = 100
numbers = [x for x in range(1, target + 1)]
ways = [0 for _ in range(target + 1)]
ways[0] = 1

for i in numbers:
    for j in range(i, target + 1):
        ways[j] += ways[j - i]



print(ways[-1] - 1)
from time import clock
from itertools import count

t0 = clock()
target = 200

shortest = [0 for _ in range(target + 1)]

""" def recurse(current = 1, known = set([1]), depth = 0):

    if depth < shortest[current]:
        print(current, depth)
        shortest[current] = depth

    for i in known:
        new = current + i
        if new > target:
            continue
        else:
            recurse(new, known | set([new]), depth + 1) """

currents = [[[1, [1]]]]
shortest[1] = 0
counter = 0

for i in count(1):
    currents.append([])
    for curr in currents[i - 1]:
        for known in curr[1]:
            new = curr[0] + known
            if new < target + 1:
                currents[i].append([new, curr[1] + [new]])
                if not shortest[new]:
                    counter += 1
                    shortest[new] = i

    print(i, counter, clock() - t0)

    for index, val in enumerate(shortest[:]):
        if val:
            try:
                if not shortest[index + 1]:
                    counter += 1
                    shortest[index + 1] = val + 1
            except IndexError:
                pass

            try:
                if not shortest[index + 2]:
                    counter += 1
                    shortest[index + 2] = val + 1
            except IndexError:
                pass
            

    if i > 1:
        currents[i - 1] = 0

    if counter == target - 1:
        break

t1 = clock()

print("Time: {}".format(t1 - t0))
print(sum(shortest[1:]))


#recurse()

print(sum(shortest[1:]))
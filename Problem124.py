from time import clock

t0 = clock()

solution_range = 100000
target = 10000

bitlist = [1 for _ in range(solution_range + 1)]

for i in range(solution_range + 1):
    if i < 2:
        continue
    else:
        if bitlist[i] != 1:
            continue

        else:
            for j in range(i, solution_range + 1, i):
                bitlist[j] *= i

rad = [[i, x] for i, x in enumerate(bitlist)]

rad = sorted(rad,key= lambda x: x[1])

print("Value: {}\tRad(Value): {}".format(*rad[target]))

t1 = clock()
print("Time: {}".format(t1 - t0))
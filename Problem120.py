from time import clock

t0 = clock()
total = 0

for a in range(3, 1001):

    r_max = (0, 0)

    for n in range(1, 2 * a, 2):
        r = (2 * a * n) % (a * a)

        if r > r_max[0]:
            r_max = (r, n)

    total += r_max[0] 

t1 = clock()
print(total)
print("Solution took {} seconds".format(t1 - t0))
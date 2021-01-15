from itertools import count
from math import sqrt

x = 1
y = 0

while True:

    counter = 0
    # I dont know how to calculate this constant but
    # it was empirically determined
    for i in count(int(x / 0.171573 ) - 2):

        j = int(i * sqrt(2))

        if j * (j - 1) == 2 * i * (i - 1):
            x = i
            y = j
            break

        counter += 1
        if counter % 1000000 == 0:
            print(counter)

    print("x: {}\ty: {}".format(x, y))
    if y > 10 ** 12:
        break
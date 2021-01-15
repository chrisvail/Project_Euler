#from itertools import combinations_with_replacement #, count
from functools import reduce
#from StandardFunctions import genprimes
from math import log, sqrt

target = 12000
limit = int(1 + (log(target) / log(2)))
k_values = [2 * target + 1 for _ in range(target + 1)]

def main():

    points = [[] for i in range(limit + 1)]
    
    points[2] = make_product([[x] for x in range(2, int(sqrt(target)) + 5)])
    #print(points[2])
    for i in range(3, limit + 1):
        points[i] = make_product(points[i - 1])
        #print(points[i])

    #print(k_values)
    print(sum(set(k_values[2:])))


def make_product(start_points):

    try:
        m = len(start_points[0]) + 1
    except IndexError:
        return []

    new_points = []
    #print(start_points)
    
    for i in start_points:
        i.append(i[-1])
        while True:
            p = product(i)

            if p > 2 * target:
                break

            else:
                new_points.append(i[:])
                s = sum(i)
                k = p - s + m
                if k <= target:
                    #print("k: {}\tlen(k_values): {}\ti: {}".format(k, len(k_values), i))
                    if k_values[k] > p:
                        k_values[k] = p
                    
                i[-1] += 1

    return new_points








def product(iterable):
    return reduce(lambda x,y: x * y, iterable)  



if __name__ == "__main__":
    main()


# int((target + (2 ** n) - 3)/ ((2 ** n) - 1)) + 2)], n):
# https://www.researchgate.net/publication/270185488_When_Does_a_Sum_of_Positive_Integers_Equal_Their_Product





































"""
def g(n, p):
    
    for s in range(n, 2 * (n - 1) + 1):
        value = (s / (p - 1)) * p
        if ((value / p > 2 and p not in powers) or (p in powers and value / p >= 2)) and value % 1 == 0:
            print("n , p, s: {}, {}, {}\tg(n, p): {}".format(n, p, s, value))
            return int(value)

        elif value > 2*n:
            print("Discarded n, p, s: {}, {}, {}".format(n,p,s))
            return inf

    print("Discarded n, p, s: {}, {}, {}".format(n,p,s))
    return inf
    
def make_product(start_points):
    try:
        length = len(start_points[0])
    except IndexError:
        return []
    new_points = []
    for i in start_points:
        i.append(i[-1])
        while True:

            v = product(i)
            if product(i) > target * 2:
                break

            k = v + length - sum(i)
            if k <= target and k_values[k] > v:
                k_values[k] = v
                print("Point: {}\tK".format(i))
            
            new_points.append(i)
            i[-1] += 1

    return new_points


def prime_factors(n):
    return None


    for r in range(2, limit + 1):
        print(r)
        for i in combinations_with_replacement([x for x in range(2, target + 1)], r):

            v = product(i)

            try:
                values[v - sum(i) + r].append(v)
            except IndexError:
                pass

    for line in values:
        print(line)
    print(sum(set([min(x) for x in values[2:]])))

"""
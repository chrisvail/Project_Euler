from fractions import Fraction as f
from itertools import count
from math import sqrt
from StandardFunctions import genprimes



def main():
    
    """ target = 1000000

    print("Factoring")

    factors = [0 for _ in range(target)]

    for i in range(1, target):
        for j in range(i, target, i):
            factors[j] += 1

    print("Finding largest square factor")

    largest_square_factor = [0 for _ in range(target)]
    for i in range(2, int(sqrt(target) + 1)):
        for j in range(i ** 2, target, i ** 2):
            largest_square_factor[j] = i

    print("Adjusting for square factors")

    for i in range(1, target):
        if largest_square_factor[i] == 0:
            continue 
        else:
            for j in range(i // largest_square_factor[i], target, i // largest_square_factor[i]):
                if j % i == 0:
                    continue 
                else:
                    factors[j] += 1

    print("Adjusting factors")

    factors = [(x + 1) // 2 for x in factors]

    print("Finding factor")

    b = [2,4,6,12,24,30,60,120,180,210,360,420,840,1260,1680,2520,4620,7560,9240,13860,18480]
    c = [2,3,5,8,11,14,23,32,38,41,53,68,95,113,122,158,203,221,284,338,365]

    for index, value in enumerate(b):
        if factors[value] != c[index]:
            print(value, factors[value], c[index])
    for i in factors:
        if i > 1000:
            print(i)
            break

    else:
        print("Failed to find factor.")
        print("Largest factor found:", factors[-1]) """


    max_counter = [0, 0]
    primes = genprimes(500000)

    """ for n in count(2, 2):
        counter = 0
        
        for y in range(n + 1, 2 * n + 1):
            a = f(1, n) - f(1, y)
            if a.numerator == 1 and a.denominator >= y:
                #print(a.denominator, y, n)
                counter += 1

        if counter > max_counter[1]:
            max_counter = [n, counter]
            print(max_counter)

            factors = []
            copy = n
            p = 0
            while copy != 1:
                if copy % primes[p] == 0:
                    copy = copy // primes[p]
                    factors.append(primes[p])
                else:
                    p += 1

            print("Factors:", factors)
            print()

        if counter > 1000:
            print(n) """

    for n in generate_ns():
        n_sqr = n * n
        counter = 0
        for a in range(1, n + 1):
            if n_sqr % a == 0:
                counter += 1
        
        if counter > max_counter[1]:
            max_counter = [n, counter]
            print(max_counter)

            factors = []
            copy = n
            p = 0
            while copy != 1:
                if copy % primes[p] == 0:
                    copy = copy // primes[p]
                    factors.append(primes[p])
                else:
                    p += 1

            print("Factors:", factors)
            print()

        if counter > 4000000:
            print(n)
            break
        

def generate_ns():
    number = []

    for _17 in range(2):
        for _13 in range(_17, 3):
            for _11 in range(_13, 4):
                for _7 in range(_11, 4):
                    for _5 in range(_7, 5):
                        for _3 in range(_5, 6):
                            for _2 in range(_3, 6):
                                a = 2 ** _2 * 3 ** _3 * 5 ** _5 * 7 ** _7 * 11 ** _11 * 13 ** _13 * 17 ** _17
                                number.append(a)

    print("Generated")
    number = sorted(number)

    print("Sorted")

    for i in number:
        yield i

if __name__ == '__main__':
    main()
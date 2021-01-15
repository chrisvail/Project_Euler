from decimal import Decimal as d
from functools import reduce

def main():

    test = sample_func(20)
    total = test[0]
    for i in range(2, 11):
        total += sequence_gen(i + 1, test[:i])
    
    print(total)


def sample_func(length):
    
    result = []

    for i in range(1, length + 1):
        result.append((1 - i + i **2 - i ** 3 + i ** 4 - i ** 5 + i ** 6 - i ** 7 + i ** 8 - i ** 9 + i ** 10))
    return result


def sequence_gen(n, nums):
    lagrange = []
    for x, y in enumerate(nums):
        x = x + 1
        top = reduce(lambda i, j: i * j, [n - a for a in range(1, len(nums) + 1) if a != x])
        bottom = reduce(lambda i, j: i * j, [x - a for a in range(1, len(nums) + 1) if a != x ])
        lagrange.append([d(top * y), d(bottom)])

    return sum([a[0] / a[1] for a in lagrange])


""" def main():

    test = sample_func(20)
    print(test[:13])
    total = 0
    for i in range(1, 12):
        func = gen_n_term_func(test[:i])
        total += func(i)
        #print(func(i + 1))
        print(' ', end = '')
        for i in range(i + 1):
            print(func(i + 1), end = ', ')

        print()
    print(total)


def sample_func(length):
    
    result = []

    for i in range(1, length + 1):
        #result.append((1 + i**2 + i**4 + i**6 + i**8 + i ** 10) -
        #              (i + i ** 3 + i ** 5 + i ** 7 + i ** 9))
        result.append((1 - i + i **2 - i ** 3 + i ** 4 - i ** 5 + i ** 6 - i ** 7 + i ** 8 - i ** 9 + i ** 10))
    return result


def gen_n_term_func(num):

    # order = len(num) - 1
    length = len(num)

    n_array = [[i ** x for x in range(length)] for i in range(1, length + 1)]
    const_array = [[x] for x in num]

    n_matrix = m.matrix(n_array)

    n_matrix = n_matrix.I

    const_matrix = m.matrix(const_array)
    #print(n_matrix * const_matrix)
    coeffs = []

    for i in n_matrix * const_matrix:
        coeffs.append(round(i.item()))

    #print(coeffs)
    return lambda x: (sum([j * (x ** i) for i,j in enumerate(coeffs)]))
"""


if __name__ == '__main__':
    main()
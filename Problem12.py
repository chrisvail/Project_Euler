# Imports sqrt function
from math import sqrt

# Returns the nth triangle number
def triangle_number(n):
    return int((n/2)*(n+1))

# Counts the number of divisors of n
def count_divisors(n):
    count = 0

    #Counts number of pairs of divisors as div1 < sqrt(n) < div2
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            count += 2

    #Adds 1 if its a perfect square
    if sqrt(n) % 1 == 0:
        count -= 1

    return count


def main(start, stop, step):

    # Sets max divider value
    maxdiv = 0

    # Goes through all values 
    for i in range(start, stop, step):

        if count_divisors(triangle_number(i)) > maxdiv:
            maxdiv = count_divisors(triangle_number(i))

            if maxdiv > 300:
                print(i, triangle_number(i), count_divisors(triangle_number(i)))
                return

def count(start):
    while True:
        yield start
        start += 1


def main2():
    triangle = 0
    for i in count(1):
        triangle += i
        if count_divisors(triangle) > 500:
            print(triangle)
            return

#Runs the main program
#main(1, 100000000, 1)
main2()
"""
while True:
    if count_divisors(triangle_number(i)) > 500:
        print(triangle_number(i))
        exit(0)
    else:
        i += 1
"""
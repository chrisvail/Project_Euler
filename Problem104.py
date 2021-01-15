from math import log10 as log
from math import sqrt

fib_50 = [1 for i in range(60)]
for i in range(2, 60):
    fib_50[i] = fib_50[i - 1] + fib_50[i - 2]

def main():

    counter = 0
    numbers = [str(x) for x in range(1, 10)]

    for index, value in enumerate(fib_last_9()):
        #if index < 320000:
        #    continue 
        if index % 100000 == 0:
            print(index)

        i = str(value)
        if all([x in i for x in numbers]):
            counter += 1
            print(counter, index + 1)
            a = fib_n(index + 1)
            if all([x in a for x in numbers]):
                print(index + 1)
                return



def fib_last_9(value1 = 1, value2 = 1):
    yield value1
    yield value2

    while True:
        value1, value2 = value2, value1 + value2

        value2 = value2 % 1000000000

        yield value2

def fib_n(n):

    root5 = sqrt(5)
    golden = (1 + root5) / 2
    log_root_5 = log(root5)
    t = n * log(golden) - log_root_5
    

    fibn = 10 ** (t - ((t // 1) - 8)) // 1

    print(fibn)
    return str(fibn)

    """ operations = []

    #breakdown = n

    while breakdown > 50:
        if breakdown % 2 == 0:
            operations.append(False)
            breakdown = breakdown // 2
        
        else:
            operations.append(True)
            breakdown = breakdown - 1

    #print(breakdown)

    fib_n = fib_50[breakdown]
    fib_n1 = fib_50[breakdown + 1]

    for i in reversed(operations):
        if i:
            fib_n, fib_n1 = fib_n1, fib_n + fib_n1
        else:
            # breakdown = breakdown * 2
            # x[2 * i] = x[i] * ((2 * x[i + 1]) - x[i])
            # x[(2 * i) + 1] = (x[i + 1] ** 2) + (x[i] ** 2)
            fib_n, fib_n1 = fib_n * ((2 * fib_n1) - fib_n), (fib_n1 ** 2) + (fib_n ** 2)

    #print(breakdown, len(operations))

    while fib_n // 1000000000 != 0:
        fib_n = fib_n // 10

    print("Done. Operations: {}\tNumbers: {}".format(len(operations), fib_n))
    return str(fib_n) """



if __name__ == '__main__':
    main()


""" x = [0 for x in range(1000000)]
x[0], x[1], x[2], x[3], x[4] = 0, 1, 1, 2, 3

print(x[:10])

for i in range(1, len(x)):
    #print(x[i])
    x[2 * i] = x[i] * ((2 * x[i + 1]) - x[i])
    x[(2 * i) + 1] = (x[i + 1] ** 2) + (x[i] ** 2)

    if i % 5000 == 0:
        print(i)



#print("Done")


from StandardFunctions import fib_generator    

numbers = [str(x) for x in range(1, 10)]

for index, value in enumerate(fib_generator()):
    #if index < 2749:
    #    continue 

    f = False
    t = False

    a = str(value)
    first = a[:9]
    last = a[-9:]

    if index % 10000 == 0:
        pass
        #print(index, len(a))

    if all([x in first for x in numbers]):
        f = True
        print(index)
        # print("First n are pandigital: F_ {}".format(index))

    if all([x in last for x in numbers]):
        t = True
        print(index)
        #print("Last n are pandigital: F_ {}".format(index))

    if f and t:
        print(index, len(a))
        break """
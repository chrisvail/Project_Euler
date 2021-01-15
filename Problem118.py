from itertools import permutations
from StandardFunctions import is_prime
from time import clock as time

primes = [[] for i in range(9)]

def main():

    t0 = time()

    partitions = [[1, 1, 1, 1, 2, 3],
                  [1, 1, 1, 1, 5],
                  [1, 1, 1, 2, 2, 2],
                  [1, 1, 1, 2, 4],
                  [1, 1, 1, 3, 3],
                  [1, 1, 1, 6],
                  [1, 1, 2, 2, 3],
                  [1, 1, 2, 5],
                  [1, 1, 3, 4],
                  [1, 1, 7],
                  [1, 2, 2, 2, 2],
                  [1, 2, 2, 4],
                  [1, 2, 3, 3],
                  [1, 2, 6],
                  [1, 3, 5],
                  [1, 4, 4],
                  [1, 8],
                  [2, 2, 2, 3],
                  [2, 2, 5],
                  [2, 3, 4],
                  [2, 7],
                  [3, 3, 3],
                  [3, 6],
                  [4, 5]]


    partition_list = []

    for i in partitions:
        part = []
        for index, j in enumerate(i):
            if index == 0:
                part.append(j)
            else:
                part.append(part[index - 1] + j)

        partition_list.append(part)

    counter = 0
    total = 0

    loop_t0 = time()
    

    for i in permutations(list(range(1, 10)), 9):

        counter += 1

        if counter % 10000 == 0:
            loop_t1 = time()
            print("Finished {} loops in {} seconds per loop".format(counter, (loop_t1 - loop_t0) / 10000))
            loop_t0 = loop_t1

        for partition in partition_list:
            part = []

            for ind, p in enumerate(partition):
                if ind == 0:
                    part.append(number(i[:p]))
                else:
                    part.append(number(i[partition[ind - 1]:p]))

            if test_part(part):
                total += 1

    t1 = time()

    print("Program took {} seconds to run".format(t1 - t0))
    print(total)



def number(i):

    num = 0
    i = reversed(i)

    for index, n in enumerate(i):
        num += n * (10 ** index)

    return num


def test_part(parts):

    for i in range(len(parts)):
        if i > 0 and parts[i] < parts[i - 1]:
            return False
        
        elif not is_prime(parts[i]):
            return False
        
    return True
    


if __name__ == '__main__':
    main()
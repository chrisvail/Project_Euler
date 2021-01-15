from math import factorial

factorials = [factorial(x) for x in range(10)]
previous_chains_length = [0 for i in range(1000000)]

def main():
    
    counter = 0

    for i in range(1, 1000000):
        if i % 10000 == 0:
            print("Completed {}\tCounter: {}".format(i, counter))
        if find_chain_length(i) == 60:
            counter += 1

    print(counter)


def find_chain_length(i):

    if previous_chains_length[i] != 0:
        return previous_chains_length[i]

    previous_numbers = []

    while i not in previous_numbers:

        previous_numbers.append(i)

        i = factorial_digit_sum(i)

        try:
            if previous_chains_length[i] != 0:
                return previous_chains_length[i] + len(previous_numbers)
        except IndexError:
            pass

    for index, value in enumerate(previous_numbers):

        try:
            previous_chains_length[value] = len(previous_numbers) - index
        except IndexError:
            pass

    return len(previous_numbers)


def factorial_digit_sum(i):

    return sum([factorials[int(x)] for x in str(i)])



if __name__ == '__main__':
    main()
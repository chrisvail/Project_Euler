

def main():
    
    line_length = 50
    total = 0

    for block_length in range(2, 5):

        total += f(block_length, line_length)

    print(total)


def f(block_length, line_length):

    numbers = [[0 for _ in range(block_length + 1)] for __ in range(line_length + 1)]

    numbers[1] = [1, 1] + [0 for _ in range(block_length - 1)]

    for index in range(2, line_length + 1):
        numbers[index][0] = numbers[index - 1][0] + numbers[index - 1][-1]
        numbers[index][1] = numbers[index - 1][0] + numbers[index - 1][-1]
        for i in range(2, block_length + 1):
            numbers[index][i] = numbers[index - 1][i - 1]

    return numbers[-1][0] + numbers[-1][-1] - 1


if __name__ == '__main__':
    main()
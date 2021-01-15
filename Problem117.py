
target = 50

numbers = [[0 for x in range(10)] for y in range(target + 1)]

numbers[1] = [1,1,0,1,0,0,1,0,0,0]

for i in range(2, target + 1):
    n = numbers[i - 1][0] + numbers[i - 1][2] + numbers[i - 1][5] + numbers[i - 1][9]
    numbers[i][0] = n
    numbers[i][1] = n
    numbers[i][2] = numbers[i - 1][1]
    numbers[i][3] = n
    numbers[i][4] = numbers[i - 1][3]
    numbers[i][5] = numbers[i - 1][4]
    numbers[i][6] = n
    numbers[i][7] = numbers[i - 1][6]
    numbers[i][8] = numbers[i - 1][7]
    numbers[i][9] = numbers[i - 1][8]

print(numbers[-1][0] + numbers[-1][2] + numbers[-1][5] + numbers[-1][9])
matrix =  []

with open("Problem81.txt") as inpt:
    for line in inpt:
        matrix.append([int(x) for x in (line.strip('\n').split(','))])

for x in range(1, 80):

    y = 0

    while True:

        if y == 0:
            matrix[y][x] += matrix[y][x - 1]

        elif x == 0:
            matrix[y][x] += matrix[y - 1][x]
            break

        elif matrix[y - 1][x] > matrix[y][x - 1]:
            matrix[y][x] += matrix[y][x - 1]

        elif matrix[y - 1][x] < matrix[y][x - 1]:
            matrix[y][x] += matrix[y - 1][x]

        else:
            assert False
        
        x -= 1
        y += 1


for y in range(1 , 80):

    x = 79

    while True:

        if matrix[y - 1][x] > matrix[y][x - 1]:
            matrix[y][x] += matrix[y][x - 1]

        elif matrix[y - 1][x] < matrix[y][x - 1]:
            matrix[y][x] += matrix[y - 1][x]

        else:
            assert False    

        if y == 79:
            break    
        
        x -= 1
        y += 1

print(matrix[-1][-1])
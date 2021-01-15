matrix =  []

with open("Problem82.txt") as inpt:
    for line in inpt:
        matrix.append([int(x) for x in (line.strip('\n').split(','))])

size = len(matrix)

for x in range(size - 2, -1, -1):

    values = []

    for y in range(size):

        route_options = []

        for i in range(size // 8):
            
            if i == 0:
                route_options.append(matrix[y][x] + matrix[y][x + 1])
            
            else:
                if 1 < i < y + 2:
                    route_options.append(sum([matrix[y - a][x] for a in range(i)]) + matrix[y - (i - 1)][x + 1])

                if 1 < i < size - y + 1:
                    route_options.append(sum([matrix[y + a][x] for a in range(i)]) + matrix[y + (i - 1)][x + 1])

        values.append(min(route_options))

    for y, number in enumerate(values):
        matrix[y][x] = number

print(min([matrix[y][0] for y in range(size)]))
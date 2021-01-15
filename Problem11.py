# Sets variables for the grid, current and max products
grid = [[0 for x in range(20)] for y in range(20)]
cprod = 0
maxprod = 0

# Generates grid in a 2d array
with open("Problem11Grid.txt", 'r') as file:
    for i in range(20):
        line = file.readline()
        line = line.strip('\n')
        line = line.split(' ')
        for j in range(20):
            line[j] = line[j].strip('0')
            if line[j] == '':
                line[j] = '0'
            line[j] = int(line[j])
            grid[i][j] = line[j] 

# Loops through all horizontal possibilities and finds max
for y in range(20):
    for x in range(17):
        cprod = grid[y][x] * grid[y][x + 1] * grid[y][x + 2] * grid[y][x + 3]
        if cprod > maxprod:
            maxprod = cprod

# Loops through all vertical options and finds max
for y in range(17):
    for x in range(20):
        cprod = grid[y][x] * grid[y + 1][x] * grid[y + 2][x] * grid[y + 3][x]
        if cprod > maxprod:
            maxprod = cprod

# Loops through one set of diagonal options
for y in range(17):
    for x in range(17):
        cprod = grid[y][x] * grid[y + 1][x + 1] * grid[y + 2][x + 2] * grid[y + 3][x + 3]
        if cprod > maxprod:
            maxprod = cprod

# Loops through second set of diagonal options
for y in range(17):
    for x in range(17):
        cprod = grid[y][x + 3] * grid[y + 1][x + 2] * grid[y +2][x + 1] * grid[y + 3][x]
        if cprod > maxprod:
            maxprod = cprod

# Prints maximum value 
print("The greatest product is: {}".format(maxprod))
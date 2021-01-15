from itertools import permutations

def main():

    matrix =  []
    upper_bound = 999999999

    with open("Problem83.txt") as inpt:
        for line in inpt:
            matrix.append([[int(x), upper_bound, False] for x in (line.strip('\n').split(','))])

    size = len(matrix)
    matrix[0][0] = [matrix[0][0][0], matrix[0][0][0], True]
    x, y = 0, 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    counter = 0

    while x != - 1 or y != - 1:
        counter += 1
        for a, b in dir:
            #print("a: {}\tb: {}".format(a, b))
            try:
                    
                if y + a >= 0 and x + b >= 0:
                    if not matrix[y + a][x + b][2] and \
                    matrix[y + a][x + b][1] > matrix[y][x][1] + matrix[y + a][x + b][0]:
                        matrix[y + a][x + b][1] = matrix[y][x][1] + matrix[y + a][x + b][0]

            except IndexError:
                continue
            
            #for line in matrix:
            #    print([x[1] for x in line])
            
        #print([x, y])
        matrix[y][x][2] = True
        x, y = find_min_index(matrix)
        if counter % 320 == 0:
            print("{}% Complete".format(counter // 64))
        #print([x, y, x != size - 1 or y != size - 1])

    print(matrix[-1][-1])

def find_min_index(matrix):

    min = [-1, -1, 99999999999]

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x][1] < min[2] and not matrix[y][x][2]:
                min = [y, x, matrix[y][x][1]]

    return (min[1], min[0])

        
if __name__ == '__main__':
    main()

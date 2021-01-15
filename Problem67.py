inpt = open("Problem67.txt", 'r')
pyr = []

for i in range(100):

    line = inpt.readline()
    line = line.strip('\n')
    line = line.split(' ')

    for number, _ in enumerate(line):

        line[number] = int(line[number].lstrip('0'))

    pyr.append(line)

for i in range(99, 0, -1):

    for j in range(len(pyr[i]) - 1):

        if pyr[i][j] < pyr[i][j + 1]:
            pyr[i -1][j] += pyr[i][j + 1]

        else:
            pyr[i -1][j] += pyr[i][j]


print(pyr[0][0])
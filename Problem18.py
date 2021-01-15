# Prepares list object for number pyramid
pyr = []

# Opens file and reads each line into the pyramid
with open("Problem18.txt", 'r') as file:
    for i in range(15):
        line = file.readline()
        # Removes line returns and splits numbers
        line = (line.strip('\n')).split(' ')

        # Loops through each number and removes leading zeros
        # Also makes the numbers into ints
        for number, _ in enumerate(line):
            line[number] = int(line[number].lstrip('0'))
        
        # Adds the line to the pyramid
        pyr.append(line)

# Loops through pyramid backwards excluding the first line
for i in range(14, 0, -1):
    # Loops through each number in the line excluding the last one
    for j in range(len(pyr[i]) - 1):
        # Takes 2 values and adds the larger one to the value above it
        if pyr[i][j] < pyr[i][j + 1]:
            pyr[i -1][j] += pyr[i][j + 1]
        else:
            pyr[i -1][j] += pyr[i][j]

# Prints out top of the pyramid which is the longest path
print(pyr[0][0])
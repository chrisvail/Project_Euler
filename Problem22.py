# Opens file and closes it at the end of the block
with open("Problem22.txt", 'r') as file:
    # Reads in file and splits it into names
    names = file.read()
    names = names.split(',')
    # Goes through names and removes quotation marks
    for index, value in enumerate(names):
        names[index] = names[index].strip('"')

# Sorts the names into order
names.sort()

# Sets variable for the total
total = 0

# Loops through names and finds name scores
for index, name in enumerate(names):
    nametot = 0
    for letter in name:
        nametot += (ord(letter) - 64)
    
    total += nametot * (index + 1)

# Prints out answer
print(total)
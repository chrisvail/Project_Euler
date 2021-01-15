# Stores one of each possible value
numset = set()

# Loops through combinations of a and b
for a in range(2, 101):
    for b in range(2, 101):
        # Adds all a^b
        numset.add(a ** b)

# Prints answer
print(len(numset))
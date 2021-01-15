# Sets variables for totals
currtotal = 0
maxtotal = 0

# Loops through all combinations of i and j below 100
for i in range(1, 100):
    for j in range(1, 100):
        # Finds digit total for i ^ j
        currtotal = sum(int(x) for x in str(j ** i))

        # Updates max total
        if currtotal > maxtotal:
            maxtotal = currtotal

# Prints answer
print(maxtotal)
# Sets variables for 2 previous positions and sum 
pos1 = 1
pos2 = 1
sum = 0

# loops constantly until over 4 million
while pos1 < 4000000:

    pos1, pos2 = pos2, pos1 + pos2

    # Adds to the total if its even and below 4 million
    if pos2 % 2 == 0 and pos2 < 4000000:
    
        sum += pos2

# Prints out answer
print("Total even fibs: {}".format(sum))
from itertools import count

# Sets variable for list of numbers
numlist = []

# Continuously loops through numbers starting at 2
for i in count(2):
    # Sets total of 5th digit powers to 0
    p = 0

    # Goes through each digit of i and adds digit ^ 5 to p
    for num in str(i):
        p += int(num) ** 5
    
    # If p and i are equal adds it to list
    if i == p:
        # adds number to list
        numlist.append(i)

    # Breaks when there is no chance that it could work
    if i // 1000000 == 1:
        break

# Prints out answer
print("Total: {}".format(sum(numlist)))
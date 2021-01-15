# Sets current sum to 0
sum = 0

# Opens file and closes it at the end of the block
with open("Problem13.txt") as file:
    # Goes through each line, removes return and adds number to the sum
    for line in file:
        line.strip('\n')
        sum += int(line)

# Prints out total answer
print("Sum total is: {}".format(sum))
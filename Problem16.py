# Creates a string of 2^1000 and sets the sum to 0
string = str(2 ** 1000)
sum = 0

# Goes through each number and adds it to the sum
for i in string:
    sum += int(i)

# Prints out answer
print(sum)
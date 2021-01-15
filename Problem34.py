from math import factorial

# Sets current total and grand total variables
total = 0
gtotal = 0

# Loops through a reasonable range of numbers
for i in range(3, 999999):

    # Finds total of factorials of digits
    total = sum([factorial(int(x)) for x in str(i)])

    # Adds it to gtotal if total equals current number
    if total == i:
        gtotal += i

# Prints out answer
print(gtotal)
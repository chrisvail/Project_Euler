from math import factorial as fac

# Finds the string of 100!
factorial = str(fac(100))
# Sets sum to 0
sum = 0

# Loops through each number and adds it to the sum
for num in factorial:
    sum += int(num)

# Prints out answer
print(sum)
def d(n):
    """
    Returns the sum of the proper divisors of n
    """
    factot = 0
    # Loops through all the proper divisors of n and tests them
    for i in range(1, n):
        if n % i == 0:
            factot += i
    
    # Returns total
    return factot


# Creates a list of all the abundant numbers
abundant =[]

# Loops through all the relevant numbers and finds d(i)
for i in range(12, 28123):
    if i < d(i):
        abundant.append(i)

print("Abundant list compiled.")

# Sets all relevant numbers to true 
numbers = [True for i in range(28123)]

# Loops through pairs of numbers until total is too big
# Sets values that can be written as abundant sum to false
for i in abundant:
    for j in abundant:
        try:
            numbers[i + j] = False
        except IndexError:
            break

print("Sums found.")

total = 0

# Sums up all values that were not set to false
for i in range(28123):
    if numbers[i]:
        total = total + i

# Prints total
print(total)
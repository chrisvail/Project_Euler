def d(n):
    """
    Sum of the proper divisors of n
    """
    factotal = 0
    # Loops through all possible divisors and adds them to total
    for i in range(1, n):
        if n % i == 0:
            factotal += i

    # Returns the total
    return factotal

# Sets variables for amicable pairs and the total
amicable = []
total = 0

# Loops through all numbers under 10000
for i in range(10000):
    # finds d() for all values and appends them to amicable list
    amicable.append(d(i))

# Loops through all numbers under 10000
for i in range(10000):
    # Attempts to find amicable pair and adds it to the total if it does
    try:
        if amicable[amicable[i]] == i:
            if amicable[i] == i:
                continue
            else:
                total += i
    # If the index is too large it passes 
    except IndexError:
        pass

# Prints out answer
print(total)

"""
for i in range(1, 10000):
    for j in range(1, i):
        if i == d(j):
            print("i: {}\tj: {}".format(i, j))
            amicable.append(i)
            amicable.append(j)

for i in amicable:
    total += i

print(i)
"""
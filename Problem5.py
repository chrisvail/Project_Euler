# Setting variables for divisors, numbers
j = 2
prime_fac_current = []
prime_fac_total = []
num = 1

# Finds prime factors for all numbers between 2 and 20
for i in range(2, 21):
    while i != 1:
        if i % j == 0:
            prime_fac_current.append(j)
            i = i // j
            j = 2
        else:
            j += 1
    
    # If there are a greater number of factors then add another to the total
    for fac in prime_fac_current:
        if prime_fac_total.count(fac) < prime_fac_current.count(fac):
            prime_fac_total.append(fac)

    # Reset the current list
    prime_fac_current = []

# Multiply out cumulative prime factors
for val in prime_fac_total:
    num = num*val

# Prints answer
print("Lowest number with factors up to 20: {}".format(num))
from Problem27 import primes as genprimes

# Sets variables required
primes = [i for i in genprimes(1000000)]
largest_with_counter = (1,1)
current_total = 0
counter = 1

# Loops through primes as a starting point
for index, value in enumerate(primes):
    # No point trying sums below the current maximum
    counter = largest_with_counter[1]
    # Finds total based on the current prime and the counter
    current_total = sum(primes[index: index + counter])
    # Loops until the total is too big
    while current_total < 1000000:
        # Breaks if the value is too large
        if value * largest_with_counter[1] > 1000000:
            break
        # If the total in primes update the largest counter
        if current_total in primes:
            largest_with_counter = current_total, counter

        # Updates counter and current total
        counter += 1
        current_total = sum(primes[index: index + counter])

# Prints answer
print(largest_with_counter)
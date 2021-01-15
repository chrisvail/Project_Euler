# Sets value  
num = 600851475143
i = 2

# Continues to loop until break condition met
while True:

    # if num = i then must be largest factor
    if num == i:
        print(num)
        break

    elif num % i == 0:
        # if it divides evenly then it must be a primes factor
        num = num // i

    else:
        # Otherwise step on to next factor
        i += 1    
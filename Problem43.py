from itertools import permutations

PRIMES = [None, 2, 3, 5, 7, 11, 13, 17]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def substringdiv(n):
    """
    Checks if successive 3 length substrings are divisible by successive primes
    """
    # Creates holding variable
    a = 0
    # Loops through substrings start index
    for i in range(1, 8):
        # Creates substring number
        a = int(''.join([n[i], n[i + 1], n[i + 2]]))
        # Checks if it divides evenly
        if a % PRIMES[i] == 0:
            continue
        else:
            return False
    
    # Returns true if it passes all tests
    return True

# Creates total variable
total = 0

# Loops through all pandigital numbers
for i in permutations(NUMBERS):
    # Discards invalid pandigitals
    if i[0] == '0':
        continue
    # Checks for substring divisibilty and adds to total
    elif substringdiv(i):
        total += int(''.join([x for x in i]))
 
# Prints out answer
print(total)
from Problem27 import primes

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def ispandigital(i):
    """
    Checks if string i is a pandigital number
    """
    # If too long it returns false
    if len(i) > 10:
        return False

    # Loops through all numbers below the lenth of the string
    for j in range(len(i)):
        if NUMBERS[j] in i:
            continue
        else:
            # Returns false if one of the numbers is missing
            return False
    
    # Returns True if all tests pass
    return True

# Loops though primes below 10 million until pandigital is found
reversedprimes = reversed([_ for _ in primes(10000000)])
for i in reversedprimes:
    if ispandigital(str(i)):
        # Prints out answer
        print(i)
        break
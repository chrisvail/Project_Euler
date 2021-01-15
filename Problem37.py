from Problem27 import primes

# Creates a list of primes below 1000000
primelist = [i for i in primes(1000000)] 


def truncatable(n):
    """
    Takes an int and checks if it is a truncatable prime.
    """
    # Returns false for 1 digit numbers
    if n // 10 == 0:
        return False
    
    # Creates temporary variable to store parts of n
    tmp = n

    # Removing right hand digits
    # Loops until tmp is a 1 digit number
    while tmp // 10 != 0:
        tmp //= 10
        if tmp in primelist:
            continue
        else:
            # Returns false if any truc not a prime
            return False

    # Removing left hand digits
    counter = 0

    # Loops until all possible left hand digits removed
    while n % (10 ** counter) != n:

        counter += 1

        if n % (10 ** counter) in primelist:
            continue
        else:
            # Returns false if trunc not a prime
            return False

    # Returns true if passes all tests
    return True


def main():
    # Sets variables 
    trunclist = []
    counter = 0

    # Loops through primes and check if its truncatable
    for prime in primelist:

        if truncatable(prime):
            trunclist.append(prime)
            # Known length of all truncatable primes so breaks out when reached
            if len(trunclist) == 11:
                break

        counter += 1

        if counter % 5000 == 0:
            print("Completed {} out of 1000000".format(counter))
    

    print(sum(trunclist))


# Runs main if program run as script
if __name__ == '__main__':
    main()
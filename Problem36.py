def is_palindrome(n):
    """
    checks if the string n is a palindrome
    """
    for index, value in enumerate(n):
        # Checks if numbers from either end are the same
        if n[index] == n[-index - 1]:
            continue
        else:
            # Returns False when not palindrome
            return False
    
    # Returns True if palindrome
    return True


def main():
    """
    Finds the sum of all double base palindromes less than 1 million
    """
    # Sets total
    total = 0

    # Loops through all numbers below 1 million
    for i in range(1, 1000000):
        b = '{0:b}'.format(i)
        # Checks for double base palindrome
        if is_palindrome(str(i)) and is_palindrome(b):
            total += i

    # Prints out answer
    print(total)


# Runs main only if program run as script
if __name__ == "__main__":
    main()
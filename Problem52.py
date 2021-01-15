from itertools import count

def multipleset(n):
    """
    Checks if multiples of n up to 6 contain the same values
    """
    # Creates a set of values to compare
    x = set([a for a in str(n)])
    # Loops through numbers from 6 to 1
    for i in range(6, 0, -1):
        # Tests if the multiple numbers are the same
        if x == set([b for b in str(n * i)]):
            continue
        else:
            return False

    # Returns true if all tests pass
    return True


def main():
    # Loops until value found
    for i in count(1):
        if multipleset(i):
            # Returns first number that passes the test
            return i


# Only runs main if program run as script
if __name__ == "__main__":
    print(main())
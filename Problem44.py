from math import sqrt

def ispent(n):
    """
    Checks if given n is a pentagonal number
    """
    if (sqrt((24 * n) + 1) + 1 )/ 6 % 1 == 0:
        return True
    else:
        return False


def main():

    # Creates placeholder variables
    i = 0
    j = 0

    # Loops through a reasonable number of numbers
    for x in range(1, 3000):
        # Loops through numbers below x
        for y in range(x, 0, -1):
            # Generates a pair of pentagonal numbers
            i = int((x * ((3 * x) - 1)) / 2)
            j = int((y * ((3 * y) - 1)) / 2)
            # Checks if sum and difference are pentagonal
            if ispent(i - j) and ispent(i + j):
                # Returns the difference
                return i - j


# Runs program only if its run as a script
if __name__ == '__main__':
    # Prints out answer 
    print(main())
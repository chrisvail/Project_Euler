# Sets constant list of all numbers
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def main():
    # Creates set for all pandigital numbers
    pandigital = set()

    # Loops through numbers in relevant range
    for i in range(1, 10000):
        # Resets joining string
        string = ''
        # Loops through all numbers between 1 and 9
        for j in range(1, 10):
            # Joins product to string
            string = ''.join([string, str(i * j)])
            # Checks for 1 to 9 pandigital and adds to set if found
            if len(string) == 9 and ispandigital(string):
                pandigital.add(int(string))
                break

            # Moves on if string is too long
            elif len(string) > 9:
                break

    # Prints out the largest value in set
    print(max(pandigital))


def ispandigital(string):
    """
    Checks if all numbers are in a string
    """
    for i in NUMBERS:
        if i in string:
            continue
        else:
            return False

    return True


# Runs main if program is run as a script
if __name__ == '__main__':
    main()
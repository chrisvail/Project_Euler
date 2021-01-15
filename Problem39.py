from math import sqrt

def main():

    # Creates list count of pythagorian triple perimeter values 
    perimeter = [0 for _ in range(0, 1001)]
    # Loops through all possible combinations for perimeters below 1000
    for a in range(1, 500):
        for b in range(1, 500):
            # Finds if c is a pythagorian triple
            c = pythag(a, b)
            # Uses 0 being false to check if its an int value
            if c:
                # Attempts to add 1 to perimeter value
                try:
                    perimeter[a + b + c] += 1
                except IndexError:
                    pass
    
    # Prints index of maximum value 
    print(perimeter.index(max(perimeter)))
        
    

def pythag(a, b):
    """
    Returns hypotenuse of a and b if c is a whole number
    Otherwise it returns 0
    """
    c= sqrt(a*a + b*b)
    # Checks if c is a whole number
    if c % 1 == 0:
        # Makes sure c is an int rather than a float
        return int(c)
    else:
        return 0


# Runs main only if program run as a script
if __name__ == '__main__':
    main()
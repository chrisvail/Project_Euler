from math import sqrt

def main():

    counter = 0

    for i in range(1, 10001):
        if continued_fraction(i) % 2 == 1:
            counter += 1

    print(counter)

def continued_fraction(x):

    """
    Calculates the continued fraction for the square root of x
    """

    # Instantiates continued fraction object
    period = [0, []]

    # Finds the first square root below x and sets it as the first number
    for i in range(x):

        # Returns 0 if x is a perfect square
        if x == i * i:
            return 0

        elif x < i * i:
            period[0] = i - 1
            break
    
    # Sets up variables required for continued fraction calculations
    n = period[0]
    numerator = period[0]
    denominator = 1

    # Loops until the continued fraction period loops
    while True:

        # Condition for looping
        if denominator == 1 and len(period[1]) > 0:
            break

        # Calculates the next values
        n = (denominator / (sqrt(x) - numerator)) // 1
        denominator = (x - (numerator * numerator)) // denominator
        numerator = abs(numerator - (denominator * n))

        # Adds value to list
        period[1].append(n)
            

    # Returns the length of the period
    return len(period[1])
            
        
if __name__ == '__main__':
    main()
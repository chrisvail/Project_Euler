from fractions import Fraction

def main():

    # Creates required variables
    frac = Fraction(0)
    counter = 0

    # Loops 1000 times
    for _ in range(1000):
        # Creates next fraction in sequence
        frac = Fraction(1, 2 + frac)
        # Adds 1 to counter if numerator is longer than denominator
        if magnitude_difference(1 + frac):
            counter += 1

    # Prints out answer
    print(counter)


def magnitude_difference(n):
    """
    Returns true if numerator is a larger magnitude that the denominator
    """
    return len(str(n.numerator)) > len(str(n.denominator))


# Runs main if program is run as a script
if __name__ == "__main__":
    main()
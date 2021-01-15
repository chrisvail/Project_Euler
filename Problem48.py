def last_ten_exp(n):
    """
    Returns the last 10 digits of n ^ n
    """
    return (n ** n) % 10000000000

def trim(n, x):
    """
    Returns the last x places in n
    """
    return n % (10 ** x)

def main():
    total = 0
    # Loops through numbers from 1 to 1000
    for i in range(1, 1001):
        # Adds the last 10 digits of i ^ i to the total
        total += last_ten_exp(i)

    # Prints answer
    print(trim(total, 10))


# Runs main only if the program is run as a script
if __name__ == '__main__':
    main()
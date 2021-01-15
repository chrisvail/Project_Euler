def main():
    # Creates a list of number of prime divider values and sets 0 and 1
    prime_divisors = [0 for _ in range(1000000)]
    prime_divisors[0], prime_divisors[1] = 1, 1

    # Loops through all numbers
    for i in range(1000000):
        # If the number has divisors it is not a prime so skip it
        if prime_divisors[i]:
            continue
        else:
            # Add 1 to all multiples of each prime number
            for j in range(i * 2, 1000000, i):
                prime_divisors[j] += 1

    # Loops through all relevant numbers
    for i in range(210, 1000000):
        # Finds first 4 consecutive numbers with 4 distinct prime divisors
        if prime_divisors[i - 3: i + 1] == [4, 4, 4, 4]:
            # Prints answer
            print(i - 3)
            break


# Runs main only if program run as script
if __name__ == '__main__':
    main()
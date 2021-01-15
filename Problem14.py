# Creates list of previously completed collatz numbers
bitlist = [0 for i in range(1000000)]

def collatz_sequence(n):
    """
    Returns the length of the collatz sequence of n
    """
    # Stores orginial value of n and starts the count at 0 
    orignaln = n
    count = 0

    # Loops until 1 is reached
    while n != 1:
        # Attempts to see if the nth value is completed
        # If it is it adds the value and returns the count
        try:
            if bitlist[n]:
                count += bitlist[n]
                break
        # If the index is too large it skips this step
        except IndexError:
            pass

        # Completes collatz steps
        if n % 2 == 0:
            n = n // 2

        else:
            n = (3 * n) + 1

        # Increases the count by 1 each loop
        count += 1

    # Adds the final count to the bitlist value 
    bitlist[orignaln] = count
    # Returns the count
    return count

# Sets variable for length, i and current length
maxlen = 0
maxi = 0
curr = 0

# Loops through all values between 2 and 1 million
for i in range(2, 1000000):
    # Calculates length of sequence
    curr = collatz_sequence(i)

    # Stores maximum length and i value
    if maxlen < curr:
        maxlen = curr
        maxi = i

# Prints out answer
print("Maximum Length: {}\tFor: {}".format(maxlen, maxi))
    
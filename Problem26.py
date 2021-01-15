# Sets variable to hold longest chain so far
maxChain = (0,0)

# Loops through all possible values of d
for i in range(1, 1000):
    # Sets values used for long division to avoid binary imprecision
    remainder = 1
    past_remainders = []
    past_remainders.append(remainder)

    # Loops until a recurring sequence of numbers is found
    # or when a complete fraction is found
    while True:
        # Finds next remainder
        remainder = (remainder * 10) % i
        
        # Checks if end of fraction and breaks
        if remainder == 0:
            break
        
        # If the remainder has already been then its a recurring sequence
        elif remainder in past_remainders:
            # Checks length against previous lengths
            if maxChain[1] < len(past_remainders) - past_remainders.index(remainder):
                maxChain = i, len(past_remainders) - past_remainders.index(remainder)
                break
            else:
                break
        
        # Adds remainder to past remainders to be checked against
        else:
            past_remainders.append(remainder)

# Prints out answer
print(maxChain)                
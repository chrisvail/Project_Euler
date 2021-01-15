# Setting variables for palindrome and divider
palin = 0
#Chose 999 as one divisor is likely to be large
i = 999

# 3 nested for loops as 3 digit product can only create
# a 6 digit palindrome.
# Starts high to find the largest
for x in range(9, -1, -1):

    for y in range(9, -1, -1):

        for z in range(9, -1, -1):

            # Concatinates x y z to make a palindrome
            palin = int("".join([str(x), str(y), str(z), str(z), str(y), str(x)]))

            # Loops through 3 digit numbers to find possible divisor
            # Otherwise it breaks when i is no longer 3 digits
            while True:
                if palin % i == 0 and palin / i < 1000:
                    print("Highest palindrome with 2 3-digit factors: {}".format(palin))
                    exit(0)
                elif i < 100:
                    i = 999
                    break
                else:
                    i -= 1
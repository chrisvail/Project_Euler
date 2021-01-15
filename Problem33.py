from fractions import Fraction as frac

# Sets total fraction
fraction = frac(1,1)

# Loops through all combinations of 3 numbers
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):

            # This would result in unity so cancelling would work
            if i == j and j == k:
                continue

            # Tests bad cancelling
            elif frac(str(j) + str(i) + '/' + str(i) + str(k)) == frac(j, k):
                fraction *= frac(j, k)

# Prints out result
print(fraction)
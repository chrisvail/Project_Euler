# Sets total constant and counter for number of ways to make it
TOTAL = 200
counter = 0

# Loops using roman numerals of value for coins
# Loop range given as a function of total
for cc in range((TOTAL // 200) + 1):
    for c in range((TOTAL // 100) + 1):
        for l in range((TOTAL // 50) + 1):
            for xx in range((TOTAL // 20) + 1):
                for x in range((TOTAL // 10) + 1):
                    for v in range((TOTAL // 5) + 1):
                        for ii in range((TOTAL // 2) + 1):
                            for i in range(TOTAL + 1):
                                # Finds total value of coins
                                sumtot = 200 * cc + 100 * c + l * 50 + xx * 20 + x * 10 + v * 5 + ii * 2 + i

                                # Adds to counter if it equals TOTAL
                                if sumtot == TOTAL:
                                    counter += 1
                                
                                # Breaks out of units loop if too big
                                elif sumtot > TOTAL:
                                    break
                            # Breaks out of 2s loop if too big
                            if 200 * cc + 100 * c + l * 50 + xx * 20 + x * 10 + v * 5 + ii * 2 > TOTAL:
                                break

# Prints out answer                              
print(counter)
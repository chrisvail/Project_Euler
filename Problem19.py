# Sets constants for the first days of each type of year
FIRSTSNORM = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
FIRSTLEAP = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

# Sets values for the count and number of days passed
count = 0
n = 0

# Loops through each year in the century
for i in range(1901, 2001):
    # Calculates if its a leap year then tests which first are Sundays
    if i % 4 == 0:
        for j in FIRSTLEAP:
            if (j + n) % 7 == 5:
                count += 1
        n += 366
    else:
        for j in FIRSTSNORM:
            if (j + n) % 7 == 5:
                count += 1
        n += 365

# Prints out answer
print(count)
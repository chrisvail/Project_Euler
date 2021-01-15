count = 0

# Counts number of times i to the power of n has a length of n
for n in range(1000):
    for i in range(1, 10):
        if len(str(i ** n)) == n:
            count += 1

print(count)
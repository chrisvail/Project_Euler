from itertools import count

# Sets starting value for string
const = '.'

# Creates a string of numbers concatenated together
# Length is limited to 1 million
for i in count(1):
    const = const + str(i)
    # Breaks when length greater than 1 million
    if len(const) > 1000000:
        break

# Finds required product
product = int(const[1]) * \
          int(const[10]) * \
          int(const[100]) * \
          int(const[1000]) * \
          int(const[10000]) * \
          int(const[100000]) * \
          int(const[1000000])

# prints answer
print(product)
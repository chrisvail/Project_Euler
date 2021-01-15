from itertools import permutations

# Sets list of numbers constant and set of products
NUMBERS = ['1','2','3','4','5','6','7','8','9']
products = set()

# Loops through all pandigital numbers
for i in permutations(NUMBERS):
    # If its xx * yy = zzzzz then add to products
    if int(''.join(i[:2])) * int(''.join(i[2:5])) == int(''.join(i[5:])):
        products.add(int(''.join(i[5:])))

    # If its x * yyyy = zzzz then add to products
    elif int(''.join(i[:1])) * int(''.join(i[1:5])) == int(''.join(i[5:])):
        products.add(int(''.join(i[5:])))

# Prints answer
print(sum(products))


"""
def pandigital9(string):
    
    Checks if the string passed in is a pandigital number
    
    currletters = set()
    if len(string) != 9 or '0' in string:
        return False
    for letter in string:
        if letter in currletters:
            return False
        else:
            currletters.add(letter)
    return True



products = set()

for i in range(2, 5000):
    for j in range(2, 5000):
        string = str(i) + str(j) + str(i * j)
        if pandigital9(string):
            products.add(i * j)
    if i % 100 == 0:
        print("Gone through {} of 5000".format(i))

print(sum(products))
"""
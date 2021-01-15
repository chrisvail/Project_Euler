from itertools import permutations

# Sets variables for cypher text, words and letters
ctext = []
words = []
letters = [x + 97 for x in range(26)]

# Reads in cypher text and conditions it
with open("Problem59.txt") as inpt:
    for line in inpt:
        ctext = line.split(',')
    
    # Converts strings to ints
    for i in range(len(ctext)):
        ctext[i] = int(ctext[i])

# Loops through all possible keys
for key in permutations(letters, 3):
    # Repeats the key more than enough times
    i = key * 500
    # Decodes cypher using tested key
    testtext = ''.join(chr(a ^ b) for a,b in zip(ctext, i))
    # Checks for common words used in english
    if 'the' in testtext and 'and' in testtext and 'that' in testtext:
        print(sum(ord(a) for a in testtext))
        
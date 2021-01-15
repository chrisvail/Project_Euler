from itertools import count

# Reads in list of words and conditions them
with open("Problem42.txt", 'r') as file:
    words = file.read()
    words = [x.strip('"') for x in words.split(',')]


def triangle_num(n):
    """
    Finds triangle numbers up to n
    """
    x = 0
    # Loops until break condition is met
    for i in count(1):
        x += i
        if x > n:
            break
        else:
            yield x


tnum = []
counter = 0

# Generates triangles below the longest possible word score
tnum = [x for x in triangle_num(364)]

# Loops through all words
for word in words:
    total = 0
    # Finds word score for current word
    total = sum([ord(letter) - 64 for letter in word])

    # Adds one to counter if word score is triangle
    if total in tnum:
        counter += 1

# Prints out answer
print(counter)
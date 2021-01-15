keys = []

with open('Problem79.txt', 'r') as inpt:
    for line in inpt:
        keys.append(line.strip('\n'))

numbers_after = [set() for _ in range(10)]
numbers = set()

for i in keys:
    numbers_after[int(i[0])].add(int(i[1]))
    numbers_after[int(i[0])].add(int(i[2]))
    numbers_after[int(i[1])].add(int(i[2]))
    numbers.add(int(i[0]))
    numbers.add(int(i[1]))
    numbers.add(int(i[2]))

guessed_key = []

numbers_after_len = [len(x) for x in numbers_after]

for i in range(10, -1, -1):
    for key, j in enumerate(numbers_after_len):
        if i == j and key in numbers:
            guessed_key.append(key)
        


#73162890

print(guessed_key)
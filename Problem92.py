seen = [0 for i in range(10000000)]
print("Generated list")

for number, i in enumerate(seen):
    if i or number == 0:
        continue

    if number % 500000 == 0:
        print("Completed {}%".format(number // 100000))

    chain = []
    while True:
        chain.append(number)
        
        if number == 1 or number == 89:
            break

        if seen[number]:
            number = seen[number]
            break

        number = sum([int(x) * int(x) for x in str(number)])


    for j in chain:
        seen[j] = number



for value, index in enumerate(seen):
    if not index:
        print(value)

print(seen.count(89))
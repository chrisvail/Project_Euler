numbers = []
predigits = 0
numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
conversions = [1000, 500, 100, 50, 10, 5, 1]
with open("Problem89.txt") as inpt:
    for line in inpt:
        line = line.strip('\n')
        total = 0
        predigits += len(line)
        for i in range(0, len(line)):
            index = numerals.index(line[i])
            try:
                if line[i + 1] in numerals[:index]:
                    total -= conversions[index]
                else:
                    total += conversions[index]
            except IndexError:
                total += conversions[index]

        numbers.append(total)

postdigits = 0
reverse_conversions = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]
for a,i in enumerate(numbers):
    
    for j in str(i):
        postdigits += reverse_conversions[int(j)]
    
    if len(str(i)) == 4 and str(i)[0] == '4':
        postdigits += 2

print(predigits - postdigits)
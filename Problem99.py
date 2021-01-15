from math import log

pairs = []
with open("Problem99.txt") as inpt:
    for index, line in enumerate(inpt):
        line = (line.strip('\n')).split(',')
        line = [int(x) for x in line]
        line.append(index + 1)
        pairs.append(line)

max = [0, 0]

for base, exponent, index in pairs:
    a = exponent * log(base)
    if max[0] < a:
        max = [a, index]

print(max)        
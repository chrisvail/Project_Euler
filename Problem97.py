number = 28433

for _ in range(7830457):
    number *= 2
    number %= 10000000000

number += 1

print(number)
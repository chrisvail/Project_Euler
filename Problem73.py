from fractions import Fraction

num_range = 12001
fraction_set = set()
b, d = 3, 2

for y in range(1, num_range):
    if y % 120 == 0:
        print(y // 120)
    for x in range(1, y):
        if (y + 1) / b <= x <= (y - 1) / d:
            fraction_set.add(Fraction(x, y))
        
        elif x / y > 0.5:
            break

print(len(fraction_set))
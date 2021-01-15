from itertools import combinations_with_replacement

checkouts = [0 for _ in range(200)]

singles = [x + 1 for x in range(20)] + [25]
doubles = [(x + 1) * 2 for x in range(20)] + [50]
triples = [(x + 1) * 3 for x in range(20)]

darts = singles + doubles + triples

for number_of_darts in [1, 2]:

    for first_darts in combinations_with_replacement(darts, number_of_darts):

        for final in doubles:
            total = sum(first_darts) + final
            checkouts[total] += 1

for single_checkout in doubles:
    checkouts[single_checkout] += 1

print(checkouts[6])
print(sum(checkouts))
print(checkouts[170])
print(sum(checkouts[:100]))
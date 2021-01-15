# Loops through all possible values where a < b < c
for a in range(1,999):

    for b in range(1,999):

        if a > b:
            continue

        for c in range(1,999):

            if b > c:
                continue

            # If the pythagorian triple equals 1000 it prints the answer
            elif a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print("a: {}\nb: {}\nc: {}\nProduct: {}".format(a,
                                                         b, c, a * b * c))
                exit(0)
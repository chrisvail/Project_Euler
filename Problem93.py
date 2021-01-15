from itertools import combinations, permutations, product

big_max = [0, []]


for numbers in combinations([x for x in range(10)], 4):

    values = set()
    for a, b, c, d in permutations(numbers, 4):

        for op1, op2, op3 in product([lambda a,b: a + b,
                                lambda a,b: a - b, 
                                lambda a,b: a * b, 
                                lambda a,b: a / b if b != 0 else 99999999], 
                                repeat = 3):

            v1 = op1(op2(op3(a, b), c), d)
            v2 = op1(op2(a, b), op3(c, d))

            if v1 % 1 == 0 and v1 > 0:
                values.add(v1)
            
            if v2 % 1 == 0 and v2 > 0:
                values.add(v2)




























    values = sorted(list(values))

    if numbers == (1,2,5, 8):
        print(values)

    flag = True
    max = 0
    for i in range(len(values) - 1):
        if values[i] + 1 != values[i + 1]:
            max = values[i]
            flag = False
            break
        
    if flag:
        max = values[-1]

    if big_max[0] < max:
        big_max = [max, numbers]
        print(big_max)

print(big_max)
    

                
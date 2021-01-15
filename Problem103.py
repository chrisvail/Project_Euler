from itertools import combinations

def main():
    prev_i_1 = 0
    a = list(valid_set_pairs(gen_disjoint_sets([1,2,3,4,5,6, 7])))
    min_sum = 256
    min_values = 0
    solutions = []

    for i in combinations(list(range(10, 100)), 7):

        if sum(i) > 255:
            continue 

        i = list(i)

        if i[0] == 34:
            break

        if i[1] != prev_i_1:
            prev_i_1 = i[1]
            print("Testing: {}".format(i))

        if i == [20, 31, 38, 39, 40, 42, 45]:
            print("Should pass this one")

        i = list(i)
        broken = False

        for x in a:
            if len(x[0]) == len(x[1]):
                if sum([i[b - 1] for b in x[0]]) == sum([i[b - 1] for b in x[1]]):
                    broken = True
                    break
                
            else:
                if sum([i[b - 1] for b in x[0]]) <= sum([i[b - 1] for b in x[1]]):
                    broken = True
                    break

        if not broken:
            solutions.append(i)
            if sum(i) < min_sum:
                print(i, sum(i))
                min_sum = sum(i)
                min_values = i

    print(min_sum, min_values)

    with open("Problem103.txt", 'w') as input:
        for x in sorted(solutions, key=lambda x: sum(x)):
            input.write(x)


    print(min_sum, min_values)



def gen_disjoint_sets(numbers):
    sets = [[[[0], [0], [0]]]]
    # sets = [[[0, 0, 0]]]

    for i in range(len(numbers)):
        n = len(sets[i]) * 3
        sets.append([])
        for j in range(n):

            a = [sets[i][j // 3][0][:], sets[i][j // 3][1][:], sets[i][j // 3][2][:] ]
            # a = [sets[i][j // 3][0], sets[i][j // 3][1], sets[i][j // 3][2]]
            if a[j % 3] == [0]:
                a[j % 3] = [numbers[i]]
            else:
                a[j % 3].append(numbers[i])

            # a[j % 3] += numbers[i]
        
            sets[i + 1].append(a)


    return sets[len(numbers)]

def valid_set_pairs(sets):
    for combination in sets:
        if combination[0] == [0] or combination[1] == [0] or \
           len(combination[1]) > len(combination[0]):
            continue
        else:
            if len(combination[1]) == len(combination[0]) and combination[1] < combination[0]:
                continue
            else:
                yield combination


if __name__ == '__main__':
    main()
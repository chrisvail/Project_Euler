from itertools import combinations

def main():
    
    a = [list(valid_set_pairs(x)) for x in gen_disjoint_sets([1,2,3,4,5,6,7])]
    #print(a[3])

    possibles = [[], [], [], [], []]

    for cmbo in combinations(list(range(10, 100)), 3):
        if sum(cmbo) > 150:
            continue
        elif cmbo[0] == 34:
            break
        
        cmbo = list(cmbo)
        broken = False

        for x in a[3]:
            if len(x[0]) == len(x[1]):
                if sum([cmbo[b - 1] for b in x[0]]) == sum([cmbo[b - 1] for b in x[1]]):
                    broken = True
                    break
                
            else:
                if sum([cmbo[b - 1] for b in x[0]]) <= sum([cmbo[b - 1] for b in x[1]]):
                    broken = True
                    break

        if not broken:
            possibles[0].append(cmbo)

    print("Found possibles")
    print(len(possibles[0]))

    for length in range(4, 8):
        print("Starting length {}".format(length))
        #print(a[length][:10])
        #print(possibles[length - 3])
        for combination in possibles[length - 4]:
            #print(combination)
            for i in range(combination[-1] + 1, combination[1] + combination[0]):
                
                cmbo = list(combination[:])
                cmbo.append(i)                

                if ((7 - length) * combination[-1]) + sum(combination) > 255:
                    break

                #print(cmbo)

                broken = False

                for x in a[length]:
                    if len(x[0]) == len(x[1]):
                        if sum([cmbo[b - 1] for b in x[0]]) == sum([cmbo[b - 1] for b in x[1]]):
                            broken = True
                            #print("Equal length", cmbo, x, sum([cmbo[b - 1] for b in x[0]]), sum([cmbo[b - 1] for b in x[1]]))
                            break
                        
                    else:
                        # print("Not equal length", cmbo, x, sum([cmbo[b - 1] for b in x[0]]), sum([cmbo[b - 1] for b in x[1]]))
                        if sum([cmbo[b - 1] for b in x[0]]) <= sum([cmbo[b - 1] for b in x[1]]):
                            broken = True
                            #print("Not Equal length", cmbo, x)
                            break


                if not broken:
                    #print(cmbo)
                    possibles[length - 3].append(cmbo)

        print(possibles[length - 3][:10])

    for i in possibles:
        print(i[:10])
        print(len(i))
        a = [sum(x) for x in i]
        print(min(a))


 



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

    return sets


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
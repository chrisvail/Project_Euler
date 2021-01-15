


def main():

    print("Loading Combinations...")
    combinations = []

    with open("Problem105.txt", 'r') as inpt:
        for line in inpt:
            a = (line.strip('\n').split(','))
            a = sorted([int(x) for x in a])
            combinations.append(a)
    print("Combinations Loaded\nGenerating Sets...")
    disjoint = gen_disjoint_sets([1,2,3,4,5,6,7,8,9,10,11,12])

    print("Sets Generated\nTriming Sets")
    for index, i in enumerate(disjoint[7:]):
        disjoint[index + 7] = trim_sets(i)
        #print(len(disjoint[index + 7]))

    counter = 0
    total = 0

    print("Trimming Complete\nTesting Combinations")
    for i in combinations:
        l = len(i)
        broken = False
        #print(l)
        for j in disjoint[l]:
            zero = sum([i[x - 1] for x in j[0]])
            one = sum([i[x - 1] for x in j[1]])
            if len(j[0]) > len(j[1]):
                #print(j)
                if zero <= one:
                    broken = True
                    break
            else:
                if zero == one:
                    broken = True
                    break

        if not broken:
            counter += 1
            total += sum(i)

    print(total, counter)


def gen_disjoint_sets(numbers):
    sets = [[[[0], [0], [0]]]]
    

    for i in range(len(numbers)):
        n = len(sets[i]) * 3
        sets.append([])
        for j in range(n):

            a = [sets[i][j // 3][0][:], sets[i][j // 3][1][:], \
                 sets[i][j // 3][2][:] ]
            
            if a[j % 3] == [0]:
                a[j % 3] = [numbers[i]]
            else:
                a[j % 3].append(numbers[i])
        
            sets[i + 1].append(a)

    return sets


def trim_sets(disjoint):

    new_disjoint = []
    disjoint_len = max([max(x) for x in disjoint[0]])
    #print(disjoint_len)

    #empty = 0
    #equals = 0
    #longers = 0
    #duplicate = 0
    #singles = 0
    #inequal = 0
    #elementwise = 0
    #other = 0

    for i in range(2, ((disjoint_len + 1) // 2) + 1):
        a = [[x for x in range(1, i + 1)], \
             [x for x in range(disjoint_len, disjoint_len - (i - 1), -1)]]

        #print(a)
        new_disjoint.append(a)

    for i in disjoint:
        # Removes empty sets
        if i[0] == [0] or i[1] == [0]:
            #empty += 1
            continue

        elif len(i[0]) == len(i[1]):
            #equals += 1
            # Removes duplicates
            if i[0][0] < i[1][0]:
                #duplicate += 1
                continue
            else:
                
                # Removes singles
                if len(i[0]) == 1:
                    #singles += 1
                    continue 
                # Removes obvious inequalities
                elif min(i[0]) > max(i[1]):
                    #inequal += 1
                    continue 
                
                # Not sure about this one
                #elif max(i[0]) != max(i[1]) + 1:
                #    other += 1
                #    continue

                # Removes bigger elementwise
                elif all([i[0][x] > i[1][x] for x in range(len(i[0]))]):
                    #elementwise += 1
                    continue

                #print(i[:2])
                else:
                    new_disjoint.append(i)

        else:
            #longers += 1
            # Removes duplicates
            """ if len(i[0]) < len(i[1]):
                continue

            else:
                new_disjoint.append(i) """
            
            continue
    
    #print("Empty: {}\tEqual: {}\tLonger: {}".format(empty, equals, longers))
    #print("Of equals:\nSingles: {}\tDuplicates: {}\tInequalities: {}\tElementwise: {}\tOther: {}\tPassed: {}".format(singles,duplicate,inequal, elementwise,other, equals - (singles + duplicate + inequal + elementwise + other)))
    return new_disjoint


if __name__ == '__main__':
    main()


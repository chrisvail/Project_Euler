from itertools import combinations
from functools import reduce
from random import randrange

def main():

    #a = gen_disjoint_sets(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    a = gen_disjoint_sets([20, 31, 38, 39, 40, 42, 45])
    #a = gen_disjoint_sets([3, 5, 6, 7])
    # print(check_disjoint(a))

    set_list = []
    
    """ for i in random_array(20, 45, 4): #combinations(list(range(20, 45)), 7):
        try:
            i = list(i)
            if i[0] + i[1] < i[-1] or sum(i) > 255:
                continue
            else:
                set_list.append([])
                a = gen_disjoint_sets(i)
                for index, j in enumerate(a):
                    if j[0] == [0] or j[1] == [0]:
                        continue 
                    elif check_valid(j):
                        continue 
                    else:
                        set_list[-1].append(index)

            if len(set_list[-1]) == 0:
                print(i)
            #print(len(set_list[-1]))
        except KeyboardInterrupt:
            set_of_errors = reduce(lambda x, y: x | y, [set(x) for x in set_list])
            #fail_list = [[reduce(lambda x, y: x & y, [set(x) for x in set_list if i in x])] for i in set_of_errors]
            #print(set_of_errors)
            #print(len(set_of_errors))
            #for index, i in enumerate(fail_list):
            #    print(index, len(i))
            #for i in set_list:
            #    print(len(i))
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            y = gen_disjoint_sets(letters[:4])
            for i in set_of_errors:
                print(y[i])

            print(len(set_of_errors))


            return """


    checked = []
    prev_i_3 = 0

    for i in combinations(list(range(20, 45)), 7):
        i = list(i)
        #print(i[0] + i[1] < i[-1])
        if i[0] + i[1] < i[-1] or sum(i) > 255:
            continue
        else:
            if i[0] != prev_i_3:
                prev_i_3 = i[0]
                print("a = gen_disjoint_sets({})".format(i))
                
            a = gen_disjoint_sets(i)
            #print(a)
            if check_disjoint(a):
                print(sum(i), i)
                a.append(checked)

    for i in checked:
        print(sum(i), i)


    """ equal_length = []
    for i in valid_set_pairs(a):
        if abs(sum(i[0]) - sum(i[1])) < 6 and \
           len(i[0]) != 1 and \
           len(i[1]) != 1 :
            print(i[0], i[1])
            counter += 1
        if len(i[0]) == len(i[1]) and len(i[0]) != 1:
            equal_length.append(i)
        
    for i in equal_length:
        a = [[chr(65 + [20, 31, 38, 39, 40, 42, 45].index(x)) for x in i[y]] for y in range(3)]
        print("Sum: {}, {}\ti: {}, {}".format(sum(i[0]), sum(i[1]), a[0], a[1]))

    print(len(equal_length))
    #print(len(list(valid_set_pairs(a)))) """



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
    #for i in sets:
        #print(len(i))
        #print(i)
        #print()


def check_disjoint(sets):

    for combination in sets:
        #print(combination)
        if combination[0] == [0] or combination[1] == [0] or \
           len(combination[1]) > len(combination[0]):
            continue

        a = sum(combination[0])
        b = sum(combination[1])

        if a == b:
            return False
        
        if len(combination[1]) != len(combination[0]):
            if a < b:
                return False

    return True


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

def check_valid(n):
    if n[0] == [0] or n[1] == [0]:
        return False
    if sum(n[0]) == sum(n[1]):
        return False
    elif len(n[0]) > len(n[1]) and sum(n[0]) < sum(n[1]):
        return False
    elif len(n[0]) < len(n[1]) and sum(n[0]) > sum(n[1]):
        return False
    else:
        return True

def random_array(a,b, size):
    while True:
            x = [0 for i in range(size)]
            while len(set(x)) != len(x):
                x = [randrange(a, b) for _ in range(size)]
            yield sorted(x)

if __name__ == '__main__':
    main()

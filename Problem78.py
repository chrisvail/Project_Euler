from itertools import count

numbers = [x for x in range(10000)]
p_list = [0 for i in range(100000)]

def main():
    for index, value in enumerate([1, 1, 2, 3, 5, 7, 11, 15, 22]):
        p_list[index] = value

    for target in range(2, 7):#count(2):
        
        ways = p(target)
        if target % 1 == 0:
            print("Ways: {}\tTarget: {}".format(ways, target))
        if target == 36:
            assert ways == 17977

        if target == 1000:
            print(ways)
            assert ways == 24061467864032622473692149727991

        if ways % 1000000 == 0:
            print("Found answer\nWays: {}\n\nTarget: {}".format(ways, target))
            break

def p(n):

    if n < 1:
        try:
            return p_list[n]
        except IndexError:
            return 0

    ''' result = sum([((-1) ** (k + 1)) * (p_list[n - (k * (3 * k - 1)) // 2] + p_list[n - (k * (3 * k + 1)) // 2])
                  for k in range(1, n)])
     '''
    result = 0
    
    for index, k in enumerate(g_pent):
        if k > n:
            break
        
        else:
            if index % 4 < 2:
                #print("result: {}\t +{}".format(result, p_list[n - k]))
                result += p_list[n - k]
                
            else:
                #print("result: {}\t -{}".format(result, p_list[n - k]))
                result -= p_list[n - k]

    p_list[n] = result    

    return result


def generalised_pents(size):

    pents_list = []

    for i in range(size):
        if i == 0:
            pents_list.append(0)

        else:
            pents_list.append((i * ( 3 * i - 1)) // 2)
            i = -i
            pents_list.append((i * ( 3 * i - 1)) // 2)

    return sorted(pents_list)

g_pent = generalised_pents(100000)[1:]

if __name__ == '__main__':
    main()
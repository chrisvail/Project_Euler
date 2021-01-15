from itertools import permutations

def main():
    maxnum = 0

    for i in permutations([_ for _ in range(1, 11)]):
        if min(i[0], i[3], i[5], i[7], i[9]) != i[0]:
            continue 

        else:
            currnum = concatenate(i)
            if len(str(currnum)) != 16:
                continue
            
            
            
            if currnum > maxnum:
                maxnum = currnum

    print(maxnum)

def concatenate(x):

    i = []

    for a in x:
        i.append(str(a))

    return int(''.join([i[0], i[1], i[2], i[3], i[2], i[4], i[5], i[4], i[6], i[7], i[6], i[8], i[9], i[8], i[1]]))

if __name__ == '__main__':
    main()
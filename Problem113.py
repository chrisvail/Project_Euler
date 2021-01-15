

def main():
    nb = gen_non_bouncy(100)

    total = 0


    for index, val in enumerate(nb):
        if index == 0:
            total += sum(val)
        else:
            total += sum(val[0] + val[1])

    total = total - (len(nb) + 3) * 9

    print(total)


def gen_non_bouncy(digits):

    nb = [[x for x in range(10)], [[x for x in range(10)], [9] + [x for x in range(9, 0, -1)]]]

    for level in range(2, digits):

        nb.append([[0 for _ in range(10)],[0 for _ in range(10)]])

        # Increasing
        for end in range(10):
            
            for index in range(end, 10):
                nb[level][0][index] += nb[level - 1][0][end]

        
        # Decreasing
        for end in range(10):

            for index in range(0, end + 1):
                nb[level][1][index] += nb[level - 1][1][end]
            

    return nb
        


if __name__ == '__main__':
    main()
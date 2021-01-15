from itertools import chain, product
from functools import reduce

def main():

    counter = -1

    with open("Problem96.txt", 'r') as inpt:
        for line in inpt:
            if line[0] == 'G':
                counter +=1
                puzzles.append([])
            else:
                puzzles[counter].append([int(x) for x in line.strip('\n')])

    for num, puzzle in enumerate(puzzles):
        variable.append([])
        for i in range(81):
            if puzzle[i // 9][i % 9] == 0:
                variable[num].append(i)

    for i in range(len(puzzles)):
        
        """ print("Solving this puzzle:")
        for line in puzzles[i]:
            for item in line:
                print(item, end = ' ')
            print()
        print() """

        if solve(i):
            """ print("Solution to above puzzle is:")
            for line in puzzles[i]:
                for item in line:
                    print(item, end = ' ')
                print()
            print() """
            print("Complete {}%".format((i + 1) * 2))
        else:
            print("Failed to solve")
    total = 0
    for i in range(len(puzzles)):
        total += puzzles[i][0][0] * 100
        total += puzzles[i][0][1] * 10
        total += puzzles[i][0][2] 
    
    print(total)



def solve(ppos, vpos = 0):
    if vpos == len(variable[ppos]):
        return True
    else:
        possible = get_possible(ppos, variable[ppos][vpos])

        if len(possible) == 0:
            return False

        else:
            for p in possible:
                puzzles[ppos][variable[ppos][vpos] // 9][variable[ppos][vpos] % 9] = p
                if solve(ppos, vpos + 1):
                    return True
            
            puzzles[ppos][variable[ppos][vpos] // 9][variable[ppos][vpos] % 9] = 0
            return False


def get_possible(ppos, pos):
    numbers = set([x for x in range(1, 10)])
    row = pos // 9
    col = pos % 9
    not_possible = set()

    not_possible = not_possible | set([x for x in puzzles[ppos][row] if x != 0])

    not_possible = not_possible	| set([x[col] for x in puzzles[ppos] if x[col] != 0])

    box = [x[(col // 3) * 3:(col // 3) * 3 + 3] for x in puzzles[ppos][(row // 3) * 3: (row // 3) * 3 + 3]]
    for layer in box:
        for item in layer:
            if item != 0:
                not_possible.add(item)
    
    return numbers - not_possible

        

if __name__ == '__main__':
    puzzles = []
    variable = []

    
    main()
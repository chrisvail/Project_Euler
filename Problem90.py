from itertools import combinations


def main():
    dice = []

    for die in combinations([x for x in range(10)], 6):
        dice.append(die)

    counter = 0
    for index, d1 in enumerate(dice):
        for d2 in dice[index:]:
            if test_squares(d1, d2):
                counter +=1
    
    print(counter)


def test_squares(d1, d2):

    if not((0 in d1 and 1 in d2) or (1 in d1 and 0 in d2)):
        return False
    
    if not((0 in d1 and 4 in d2) or (4 in d1 and 0 in d2)):
        return False

    if not(((0 in d1 and 9 in d2) or (9 in d1 and 0 in d2)) or
          ((0 in d1 and 6 in d2) or (6 in d1 and 0 in d2))):
        return False

    if not(((1 in d1 and 6 in d2) or (6 in d1 and 1 in d2)) or
          ((1 in d1 and 9 in d2) or (9 in d1 and 1 in d2))):
        return False

    if not((2 in d1 and 5 in d2) or (5 in d1 and 2 in d2)):
        return False

    if not(((3 in d1 and 6 in d2) or (6 in d1 and 3 in d2)) or
          ((3 in d1 and 9 in d2) or (9 in d1 and 3 in d2))):
        return False

    if not(((4 in d1 and 9 in d2) or (9 in d1 and 4 in d2)) or
          ((4 in d1 and 6 in d2) or (6 in d1 and 4 in d2))):
        return False

    if not((8 in d1 and 1 in d2) or (1 in d1 and 8 in d2)):
        return False
    
    return True

if __name__ == '__main__':
    main()
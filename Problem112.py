from itertools import count

def main():

    nb = 0

    for i in count(1):

        if is_increasing(i):
            nb += 1
        
        elif is_decreasing(i):
            nb += 1


        if nb / i == 0.01:
            print(i)
            break


def is_increasing(i):
    
    while i >= 10:

        if i % 10 < (i // 10) % 10:
            return False

        else:
            i = i // 10

    return True


def is_decreasing(i):

    while i >= 10:

        if i % 10 > (i // 10) % 10:
            return False

        else:
            i = i // 10

    return True



if __name__ == '__main__':
    main()
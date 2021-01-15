from math import e
from fractions import Fraction

def main():

    frac_list = continued_fraction(100)
    frac = Fraction(0)

    for i in reversed(frac_list[1:]):

        frac = Fraction(1, i + frac)

    frac = frac + frac_list[0]
    print(frac_list[:20])


    print(sum(int(x) for x in str(frac.numerator)))


def continued_fraction(term):

    frac_list = []

    for i in range(term):

        if i % 3 == 2:
            frac_list.append(((i + 1) // 3) * 2)
        
        elif i == 0:
            frac_list.append(2)
        
        else:
            frac_list.append(1)

    return frac_list


if __name__ == '__main__':
    main()
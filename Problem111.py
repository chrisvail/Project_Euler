from StandardFunctions import is_prime
from itertools import permutations, combinations_with_replacement

DIGITS = 10


def main():

    s = [0 for _ in range(10)]
    for d in range(10):
        
        n = DIGITS
        
        while s[d] == 0:
          
            for number in gen_repeated_digits(d, n):
                
                if is_prime(number):
                    s[d] += number

            n -= 1

    print(sum(s))
                


def gen_repeated_digits(d, n):

    length = DIGITS - n
    numbers = [x for x in range(10) if x != d]
    
    for other in combinations_with_replacement(numbers, length):
        yielded = set()
        for positions in permutations(range(DIGITS), length):
            repeat = [d for _ in range(DIGITS)]

            for index, p in enumerate(positions):
                repeat[p] = other[index]

            if repeat[0] == 0 or repeat[-1] % 2 == 0:
                continue 

            num = int(''.join(str(i) for i in repeat))

            if num in yielded:
                continue 

            yielded.add(num)

            yield num


if __name__ == '__main__':
    main()
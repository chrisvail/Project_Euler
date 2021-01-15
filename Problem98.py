from math import sqrt

def main():
    with open("Problem98.txt", 'r') as file:
        words = file.read()
        words = [[a for a in x.strip('"')] for x in words.split(',')]
    
    print("Read words")

    anagrams = []

    for index, word1 in enumerate(words):
        for word2 in words[index + 1:]:
            if sorted(word1) == sorted(word2):
                anagrams.append([word1, word2])

    print("Generated anagrams")
    anagrams = sorted(anagrams, key=lambda x: len(x[0]), reverse=True)

    

    for word1, word2 in anagrams:
        print(''.join(word1), ''.join(word2))
        l = len(word1)
        squares = []
        for i in range(int(sqrt(10 ** (l - 1))), int(sqrt(10 ** l))):
            if len(set([x for x in str(i * i)])) == l:
                squares.append(i * i)

        print(squares[:10])

        for n in reversed(squares):
            if reordered_number(word1, word2, n) in squares:
                print(n)
                return
            elif reordered_number(word2, word1, n) in squares:
                print(n)
                return

    

    print(len(squares))    


def reordered_number(word1, word2, num):
    
    order = []
    
    for i in word1:
        order.append(word2.index(i))

    number = [x for x in str(num)]
    new_number = [number[i] for i in order]
    new_number = int(''.join(new_number))
    return new_number

    

if __name__ == '__main__':
    main()
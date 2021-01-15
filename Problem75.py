#from numpy import matrixlib as np
#from sys import setrecursionlimit
#from itertools import chain
from math import sqrt
from StandardFunctions import gcd
''' 
setrecursionlimit(10000)

class Pythagorian_triple_tree():

    def __init__(self, max_triple_sum, triple = np.matrix("3;4;5")):

        self.generator_matrices = [np.matrix('1, -2, 2 ; 2, -1, 2 ; 2, -2, 3'),
                                   np.matrix('1, 2, 2 ; 2, 1, 2 ; 2, 2, 3'),
                                   np.matrix('-1, 2, 2 ; -2, 1, 2 ; -2, 2, 3')]

        self.max_triple_sum = max_triple_sum
        self.triple = triple
        self.children = []

        for i in self.generator_matrices:

            a = i * triple
            #print("a: {}\tType: {}\nelement_sum: {}\tType: {}\n".format(a.tolist(), type(a), element_sum_a, type(element_sum_a)))

            if (np.matrix("1,1,1") * a).item() < max_triple_sum:
                self.children.append(Pythagorian_triple_tree(self.max_triple_sum, a))
            


    def __repr__(self):
        return "Pythagorian triple node: {}".format(self.triple.tolist())

    def _gen_primative_triples(self):

        if self.children == []:
            return [self.triple]
        
        else:
            triples_below = list(chain.from_iterable([i._gen_primative_triples() for i in self.children]))
            triples_below.append(self.triple)

            return triples_below


    def gen_triples(self):
        
        for i in self._gen_primative_triples():
            a = i
            while (np.matrix("1,1,1") * a).item() < self.max_triple_sum:
                yield a
                a += i


    def size(self):
        if self.children == []:
            return 1
        else:
            return sum([x.size() for x in self.children]) + 1
 '''
    


def main():

    ''' print("a = Pythagorian_triple_tree(1500000)")
    a = Pythagorian_triple_tree(1500001)

    #print(a)

    #print(a.size())

    lengths = [0 for _ in range(1500001)]
    for i in a.gen_triples():
        lengths[(np.matrix("1,1,1") * i).item()] += 1

    print(sum([x == 1 for x in lengths])) '''

    limit = 1500001
    lengths = [0 for _ in range(1500001)]

    for m in range(2, int(sqrt(limit / 2)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = (m * m) - (n * n)
                b = 2 * m * n
                c = (m * m) + (n * n)
                if (a * a) + (b * b) == c * c:
                    p = a + b + c
                    
                    while p < limit:
                        lengths[p] += 1
                        p += a + b + c


    print(sum([x == 1 for x in lengths]))



if __name__ == '__main__':
    main()
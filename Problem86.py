from math import sqrt
from StandardFunctions import gcd
from itertools import count

def gen_pyth(limit):

    a_values = [[] for _ in range(limit + 1)]
    b_values = [[] for _ in range(limit * int(sqrt(limit)))]

    for m in range(2, int(sqrt(limit / 2)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = (m * m) - (n * n) if (m * m) - (n * n) < 2 * m * n else 2 * m * n
                b = (m * m) - (n * n) if (m * m) - (n * n) > 2 * m * n else 2 * m * n
                c = (m * m) + (n * n)
                if (a * a) + (b * b) == c * c:
                    # p = a + b + c
                    x , y, z = a, b, c
                    while x <= limit:
                        # lengths[p] += 1
                        a_values[x].append(y)
                        b_values[y].append(x)
                        # p += a + b + c
                        x += a
                        y += b
                        z += c

    return (a_values, b_values)

def main():
    target = 1000000
    
     
    alphas, betas = gen_pyth(target // 10)
    print("Done")
    #for value, beta in enumerate(alphas):
    #    print([value, beta])
    int_paths = [0 for _ in range(len(alphas))]

    for i in count(1):
        total = 0
        for beta in alphas[i]:
            if beta % 2 == 0:
                addition = (beta // 2) - (beta - i) + 1
            else:
                addition = ((beta - 1) // 2) - (beta - i) + 1
            
            if addition > 0:
                total += addition
        
        for alpha in betas[i]:
            if alpha % 2 == 0:
                addition = (alpha // 2)
            else:
                addition = ((alpha - 1) // 2)
            
            if addition > 0:
                total += addition

        assert total >= 0

        int_paths[i] += total + int_paths[i - 1]
        # print([i, int_paths[i], total])
        if int_paths[i] > target:
            print(i, int_paths[i])
            return


    ''' 
    for limit in count(1):
        total = 0
        successes = []
        for c in range(1, limit + 1):
            for b in range(1, c + 1):
                for a in range(1, b + 1):
                    if sqrt(c * c + (a + b) ** 2) % 1 == 0:
                        total += 1
                        successes.append([a,b,c])
                    #if (c, a + b) in triples:
                    #    total += 1

        print([limit, total, successes])
        if total > target:
            print(limit)
            break '''
   
if __name__ == '__main__':
    main()
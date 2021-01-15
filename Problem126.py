from itertools import combinations_with_replacement
from time import clock

def take_1():

    n_max = 10000

    c_n = [0 for _ in range(n_max + 1)]
    test = []
    last = 0
    t0 = 0
    print("dimension < {}\tm < {}".format((n_max - 1) // 4, int(((n_max - 2) / 4) ** 0.5)))

    for x, y, z in combinations_with_replacement([x for x in range(1, (n_max - 1) // 4)], 3):

        for m in range(1, int(((n_max - 2) / 4) ** 0.5)):
            n = 4*m**2 + 4*(x + y + z - 3)*m + 2*(x*y + x*z + y*z - 2*(x + y + z) + 4)

            if n < n_max + 1:
                c_n[n] += 1
            
            else:
                break

            if n == 154:
                test.append([m, x, y, z])

        if x != last:
            t1 = clock()
            print(x, c_n[154], c_n.index(max(c_n)), max(c_n), t1 - t0)
            last = x
            t0 = t1
        

    for i, v in enumerate(c_n):
        if v != 0 and v in [10,100,1000]:
            print("{}: {}".format(i, v))
            pass

    for m, x, y, z in test:
        print("m: {}\tx: {}\ty: {}\tz: {}\tsum: {}  \tproduct: {}\tcross product: {}".format(m**2, x, y, z, x+y+z, m*m*x*y*z, x*y + x*z + y*z))



def main():

    n_max = 20000
    t0 = clock()
    c_n = [0 for _ in range(n_max + 1)]
    print("dimension < {}\tm < {}".format((n_max - 1) // 4, int(((n_max - 2) / 4) ** 0.5)))

    for x in range(1, int((n_max - 2) / 4) + 2):
        
        for y in range(x, int((n_max - 2*x) / (2*x + 2)) + 2):
            for z in range(y, int((n_max - 2*x*y) / (2*x + 2*y)) + 2):
                for m in range(1, 100000):
                    n = 4*m**2 + 4*(x + y + z - 3)*m + 2*(x*y + x*z + y*z - 2*(x + y + z) + 4)

                    if n < n_max + 1:
                        c_n[n] += 1
                    else:
                        break
                 


        

    for i, v in enumerate(c_n):
        if v == 1000:
            print("{}: {}".format(i, v))
            break

    print("Time: {}".format(clock() - t0))


if __name__ == '__main__':
    main()
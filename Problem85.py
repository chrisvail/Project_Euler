from itertools import count

def main():

    best = [2000000, 0 , 0]

    for n in count(1):
        for m in range(n + 1):
            total = sum([sum([(n + 1 - x) * (m + 1 - y) for x in range(1, n + 1)]) for y in range(1, m + 1)])
            if abs(total - 2000000) < best[0]:
                best = [abs(total - 2000000), n, m]
                if best[0] <= 2:
                    print("Within 2")
                    print("Closest answer is where:\n\tn = {}\n\tm = {} \
                    \nTherefore the answer is: {}".format(best[1], best[2], best[1] * best[2]))
                    return 0

if __name__ == "__main__":
    main()

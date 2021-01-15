"""
total = 2
x = 3
div = 3

while x < 2000000:
    while True:
        if x == div:
            total += x
            print("Prime added: {}".format(x))
            break
        elif x % div == 0:
            break
        else:
            div += 2
        
    x += 2
    div = 3
"""
"""
total = 5
x = 5
primes = [2,3]
div = 3
looper = True
primefac = False

while x < 2000000:
    while True:
        if looper:
            for primediv in primes:
                if x % primediv == 0:
                    primefac = True
                    break
            looper = False
        else:
            if x == div:
                total += x
                print("Prime added: {}".format(x))
                primes.append(x)
                break
            elif x % div == 0:
                break
            else:
                div += 2
        if primefac:
            primefac = False
            break
            
    x += 2
    div = primes[-1]
    looper = True
        
        


print("Sum of primes below 2 million: {}".format(total))
"""

# Creates a list of boolean values 2 million digits long
n = 2000000

# Sets all bits to true
bitlist = [True for i in range(n)]

# Starts off prime list and sum
primes= [2]
p = 3

# Sets all multiples of primes to false making any true value a prime
for i in range(4, n, 2):
    bitlist[i] = False

while p < n:
    if bitlist[p]:
        primes.append(p)
        for i in range(p * 2, n, p):
            bitlist[i] = False
    p += 2

# Prints answer
print("Sum of primes less than 2 million: {}".format(sum(primes)))
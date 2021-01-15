
"""
Old solution with long running time
Done using trial division
i = 1
x = 3
div = 3

while i != 10001:
    while True:
        if x == div:
            i += 1
            break
        elif x % div == 0:
            break
        else:
            div += 1
        
    x += 2
    div = 3
"""

# Reasonable upper limit for 10,001st prime
n = 1000000

# Creates a list of boolean values whos index represents a number
bitlist = [True for i in range(n)]

# Creates a list of prime numbers and a first prime
primes = [2]
p = 3

# Sets all multiples of primes to false so true values represent primes
for i in range(4, n, 2):
    bitlist[i] = False

while p < n:
    if bitlist[p]:
        primes.append(p)
        for i in range(p * 2, n, p):
            bitlist[i] = False
    p += 2

# Prints out the answer
print("10001th prime number is: {}".format(primes[10000]))
from Problem27 import primes

# Sets variables for list of primes and circular primes
prime = [i for i in primes(1000000)]
cprime = []

# Sorts primes into sizes and then tests if circular prime
# Adds circular primes to cprime list
for i in prime:

    if i // 10 == 0:
        
        cprime.append(i)

    elif i // 100 == 0:
        s = str(i)
        if int(s[1] + s[0]) in prime:
            
            cprime.append(i)

    elif i // 1000 == 0:
        s = str(i)
        if int(s[1:] + s[0]) in prime and \
            int(s[2] + s[:2]) in prime:

            cprime.append(i)
            
    elif i // 10000 == 0:
        s = str(i)
        if int(s[1:] + s[:1]) in prime and \
            int(s[2:] + s[:2]) in prime and \
            int(s[3:] + s[:3]) in prime:

            cprime.append(i)

    elif i // 100000 == 0:
        s = str(i)
        if int(s[1:] + s[:1]) in prime and \
            int(s[2:] + s[:2]) in prime and \
            int(s[3:] + s[:3]) in prime and \
            int(s[4:] + s[:4]) in prime:
            
            cprime.append(i)

    elif i // 1000000 == 0:
        s = str(i)
        if int(s[1:] + s[:1]) in prime and \
            int(s[2:] + s[:2]) in prime and \
            int(s[3:] + s[:3]) in prime and \
            int(s[4:] + s[:4]) in prime and \
            int(s[5:] + s[:5]) in prime:
            
            cprime.append(i)

# Prints out number of circular primes
print(len(cprime))        
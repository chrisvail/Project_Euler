# Sets high, low and n value for fib sequence
low = 1
high = 1
n = 2

# Continuously loops until break condition met 
while True:
    # Increments n and gets next fib number
    low, high = high, high + low
    n += 1 

    # If the current fib number is over 1000 digits break
    if len(str(high)) == 1000:
        # Prints answer
        print("n: {}\tvalue: {}".format(n, high))
        break
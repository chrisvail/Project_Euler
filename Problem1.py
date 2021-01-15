#Sets total to 0
sum = 0

# Goes through every number up to 1000 and adds it if is divisible by 3 or 5
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

#Prints out the total 
print(sum)
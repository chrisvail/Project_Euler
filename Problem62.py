from itertools import permutations, count

def main():
    
    # Instantiates a list of sorted sets of cube digits
    cubeset = []

    print("Starting cube set")

    # Adds data to cube set
    for i in range(345, 10000):
        sortlist = [_ for _ in str(i ** 3)]
        sortlist = sorted(sortlist)
        cubeset.append(sortlist)
        
    print("Starting permutations")
    
    # Loops through all of cubeset and counts the number of occurences of the sorted list
    for index, i in enumerate(cubeset):
        if index % 500 == 0:
            print(index)
        counter = cubeset.count(i)
        # If there are 5 lists it prints the answer
        if counter == 5:
            print((index + 345) ** 3)
            return 



if __name__ == '__main__':
    main()
def main():

    """
    Finds solution to Project Euler Problem 61
    """

    # Loops through all octal numbers
    for i in numbers[5]:
        solution[5] = i

        # Finds solution and prints out answer
        if find_next(5, 1):
            print(solution)
            print(sum(solution))


def find_next(last, length):
    """
    Finds a series of 6 numbers that are cyclical and in different figurates
    """

    # Loops through all non taken figurate sets
    for index, i in enumerate(solution):
        if i != 0:
            continue
        

        # Goes through each number in set
        for j in numbers[index]:

            # Checks the solution isnt a part of the solution already
            ''' unique = True
            for k in solution:
                if j == k:
                    unique = False
                    break '''
                
            # Adds possible answer to built solution if cyclical
            if is_cyclical(j, solution[last]):
                solution[index] = j

                # If long enough checks it is completely cyclical and returns
                if length == 5:
                    if is_cyclical(solution[5], solution[index]):
                        return True

                # Otherwise tries to find the next answer in the chain
                if find_next(index, length + 1):
                    return True
        
        # Otherwise resets the solution
        solution[index] = 0

    return False

def is_cyclical(n, m):
    """
    Checks if last 2 digits in int n are first 2 digits in int m
    """
    return n // 100 == m % 100
    

def four_digit_tris():

    """
    Returns a list of triangle numbers that are 4 digits long
    """

    tris = []
    counter = 1

    while True:
        tri = (counter * (counter + 1)) / 2
        counter += 1
        if tri < 1000:
            continue
        elif tri >= 10000:
            break
        else:
            tris.append(int(tri))
        
    
    return tris


def four_digit_squares():

    """
    Returns a list of square numbers that are 4 digits long
    """

    squares = []
    counter = 1

    while True:
        square = counter * counter
        counter += 1
        if square < 1000:
            continue
        elif square >= 10000:
            break
        else:
            squares.append(int(square))
    
    return squares

def four_digit_pents():

    """
    Returns a list of pentagonal numbers that are 4 digits long
    """

    pents = []
    counter = 1

    while True:
        pent = (counter * (3 * counter - 1)) / 2
        counter += 1
        if pent < 1000:
            continue
        elif pent >= 10000:
            break
        else:
            pents.append(int(pent))
    
    return pents


def four_digit_hexs():

    """
    Returns a list of hexagonal numbers that are 4 digits long
    """

    hexs = []
    counter = 1

    while True:
        hexa = (counter * (2 * counter - 1))
        counter += 1
        if hexa < 1000:
            continue
        elif hexa >= 10000:
            break
        else:
            hexs.append(int(hexa))
    
    return hexs


def four_digit_heps():

    """
    Returns a list of heptagonal numbers that are 4 digits long
    """

    heps = []
    counter = 1

    while True:
        hep = (counter * (5 * counter - 3)) / 2
        counter += 1
        if hep < 1000:
            continue
        elif hep >= 10000:
            break
        else:
            heps.append(int(hep))
    
    return heps


def four_digit_octs():

    """
    Returns a list of octal numbers that are 4 digits long
    """

    octs = []
    counter = 1

    while True:
        octa = (counter * (3 * counter - 2))
        counter += 1
        if octa < 1000:
            continue
        elif octa >= 10000:
            break
        else:
            octs.append(int(octa))
    
    return octs


if __name__ == '__main__':
    
    # Creates a list of each type of figurate number
    numbers = [four_digit_tris(),
               four_digit_squares(),
               four_digit_pents(),
               four_digit_hexs(),
               four_digit_heps(),
               four_digit_octs()]

    # Creates solution list            
    solution = [0 for i in range(6)]

    main()




"""  
def search_cyclical(figurates = [], numbers = []):

    n = len(numbers)

    if len(numbers) == 6 and is_cyclical(numbers[-1], numbers[0]):
        print(numbers[0])
        print(numbers[-1])
        print(numbers)
        print(is_cyclical(numbers[0], numbers[-1]))
        print()
        return sum(numbers)             

    value = "This should never appear anywhere"

    for fig in ["octs", "heps", "hexs", "pents", "squares", "tris"]:
        
        if fig not in figurates:

            for i in dictionary[fig]:

                if numbers == []:

                    numbers.append(i)
                    figurates.append(fig)
                    
                    #print("Fig: {}\nFigurates: {}\nNumbers: {}".format(fig, figurates, numbers))
                    print(["TOP", value, numbers])
                    value = search_cyclical(figurates, numbers)
                    print([value, numbers])
                    if value != 0:
                        print(value)
                        return value
                    
                    else:
                        numbers = numbers[:-1]
                        figurates = figurates[:-1]

                else:

                    if is_cyclical(numbers[-1], i):
                        
                        numbers.append(i)
                        figurates.append(fig)
                        
                        #print("Fig: {}\nFigurates: {}\nNumbers: {}".format(fig, figurates, numbers))
                        print(["TOP",value, numbers])
                        value = search_cyclical(figurates, numbers)
                        print([value, numbers])
                        if value != 0:
                            print(value)
                            return value
                        
                        else:
                            numbers = numbers[:-1]
                            figurates = figurates[:-1]
                        
                #figurates = figurates[:-1]
    print(numbers)
    numbers = numbers[:n]
    print(numbers)
    return 0
"""

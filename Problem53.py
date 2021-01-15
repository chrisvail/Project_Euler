def pascaltri(n):
    """
    Returns a pascal triangle of size n
    """
    # Creates variable for triangle
    pascal = [[1]]
    # Loops through required lines
    for y in range(1, n + 1):
        # Adds a new line
        pascal.append([])
        # Loops through all positions required to fill line
        for x in range(y + 1):
            # Fills line
            if x != 0 and x != y:
                pascal[y].append(pascal[y - 1][x] + pascal[y - 1][x - 1])
            else:
                pascal[y].append(1)

    # Returns the pascal triangle as a list of lists
    return pascal


# Only runs if program run as script
if __name__ == "__main__":
    counter = 0
    # Goes through lines in triangle
    for line in pascaltri(100):
        # Loops through values in lines and sums values over 1 million
        for value in line:
            if value > 1000000:
                counter += 1

    # Prints answer
    print(counter)
    
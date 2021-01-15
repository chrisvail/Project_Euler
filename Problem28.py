# Creates constant vectors to create a spiral
VECTORS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def make_spiral(n):
    """
    Generates an Ulam spiral of side length n assuming n is odd
    """
    # Checks that input is odd otherwise exits
    if n % 2 == 0:
        raise ValueError("Non odd input")
    spiral = [[0 for _ in range(n)] for __ in range(n)]

    # Sets coordinates to the middles and direction to 0
    y = (n // 2)
    x = (n // 2)
    dircount = 0

    # Loops through number of numbers in the spiral
    for num in range(1, (n * n) + 1):
        # Places digit in correct position
        spiral[y][x] = num
        # Attempts to adjust vectors and handles with index errors
        try:
            if spiral[y + VECTORS[dircount % 4][0]][x + VECTORS[dircount % 4][1]] == 0:
                y += VECTORS[dircount % 4][0]
                x += VECTORS[dircount % 4][1]
                dircount += 1
            else:
                y += VECTORS[(dircount % 4) - 1][0]
                x += VECTORS[(dircount % 4) - 1][1]
        except IndexError:
            y += VECTORS[(dircount % 4) - 1][0]
            x += VECTORS[(dircount % 4) - 1][1]

    # Returns a spiral as a nested list
    return spiral

def total_diagonals(spiral):
    """
    Finds the sum of the diagonal values in a square matrix
    """
    # Sets up total
    total = 0
    # Goes through each line and adds diagonal values to the total
    for index, value in enumerate(spiral):
        total += value[index] + value[-index - 1]
        # Makes sure the middle value is only counted once
        if index == len(value) // 2:
            total -= value[index]        

    # Returns the sum total
    return total 


# Finds the total of a 1001 side length Ulam spiral diagonals if run as a script
if __name__ == "__main__":
    print(total_diagonals(make_spiral(1001)))
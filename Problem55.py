from Problem36 import is_palindrome

# Creates a list of boolean values representing each number
numbers = [True for i in range(1,10001)]
prevnum = []

for index, value in enumerate(numbers):
    # Sets number variable and a flag that says if a palindrome is reached
    num = index
    flag = False
    # Given that 51 times is enough to tell if lycherel number
    for _ in range(51):
        # Completes reverse and add process
        num = num + int(str(num)[::-1])
        # Checks if palindrome and breaks if it is. Also adjusts flag
        if is_palindrome(str(num)):
            flag = True
            break

    # If no palindrome reached then number set to false
    if not flag:
        numbers[index] = False

# Sets counter variable
counter = 0
# Loops through numbers and counts lychrel numbers
for i, v in enumerate(numbers):
    if not v:
        counter += 1

# Prints answer
print(counter)
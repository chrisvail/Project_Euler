# Sets constants for creating numbers
units_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
           "Eighteen", "Nineteen"]
tens_words = ["filler","Ten" , "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
specials_words = ["Hundred", "Thousand", "and"]

# Creates a list of lengths of words in strlist
def list_len(strlist, numlist):
    for value in strlist:
            numlist.append(len(value))

# Lists for use in list_len()
units = []
tens = []
specials = []

# Creating lists of the length of words
list_len(units_words, units)
list_len(tens_words, tens)
list_len(specials_words, specials)

# Sets counter to 0
counter = 0

# Adds total characters to global counter
def summation(listnum):
    for num in listnum:
        global counter
        counter += num

# Loops through the first 1000 numbers and generates lengths
for i in range(1, 1001):
    if i < 20:
        summation([units[i]])

    elif i < 100:
        if i % 10 == 0:
            summation([tens[i // 10]])
        else:
            summation([tens[i // 10], units[i % 10]])
    else:
        if i == 1000:
            summation([units[1], specials[1]])
        elif i % 100 == 0:
            summation([units[i // 100], specials[0]])
        elif i % 10 == 0:
            summation([units[i // 100], specials[0], specials[2], tens[(i // 10) % 10]])
        elif i % 100 < 20:
            summation([units[i // 100], 
                            specials[0], specials[2], 
                            units[i % 100]])
        else:
            summation([units[i // 100], 
                            specials[0], specials[2], 
                            tens[(i // 10) % 10],
                            units[i % 10]])

# Prints out the answer
print(counter)
def hands_won():
    """
    Returns the number of hands won by player 1 in text file
    """
    # Sets variables
    hands = []
    counter = 0

    # Reads in hands
    with open("Problem54.txt") as inpt:
        for line in inpt:
            hands.append((line.strip('\n')).split(' '))

    # Calculates the card values for all cards
    hands = value(hands)
    
    # Loops through all hands and counts player 1 wins
    for hand in hands:
        # Adds 1 to counter if player 1 wins
        if compare_hands(hand_value(hand[:5]), hand_value(hand[5:])):
            counter += 1

    # Returns number of player 1 wins
    return counter


def value(hands):
    """
    Returns hands as numeric values instead of cards
    """
    # Loops through all hands 
    for i, hand in enumerate(hands):
        # Loops through cards in hand
        # Assigns numbers for suits and values
        for j, card in enumerate(hand):
            cardval = 0
            #deal with suit
            if card[-1] == 'C':
                cardval += 100
            elif card[-1] == 'H':
                cardval += 200
            elif card[-1] == 'S':
                cardval += 300
            else:
                cardval += 400
            #deal with value
            if card[0] == 'A':
                cardval += 14
            elif card[0] == 'K':
                cardval += 13
            elif card[0] == 'Q':
                cardval += 12
            elif card[0] == 'J':
                cardval += 11
            elif card[0] == 'T':
                cardval += 10
            else:
                cardval += int(card[0])            

            # Card in hand into value
            hands[i][j] = cardval

    # Returns list of hands as values
    return hands


def hand_value(hand):
    """
    Returns all relevant information required to evaluate who wins a hand
    """
    # Creates list of suits and values and numbers of each value
    suits = [x // 100 for x in hand]
    val = sorted([x % 100 for x in hand])
    vallist = [0 for _ in range(15)]
    for i in val:
        vallist[i] += 1

    # Creates dictionary object that describes the hand
    handdict = {"Singles": [],
                "Pairs": [],
                "Threes": [],
                "Fours": [],
                "Straight": False,
                "Flush": False }    

    # Populates dictionary for multiple cards using numbers of each value
    for i in range(2, 15):
        if vallist[i] == 2:
            handdict["Pairs"].append(i)
        elif vallist[i] == 3:
            handdict["Threes"].append(i) 
        elif vallist[i] == 4:
            handdict["Fours"].append(i)
        elif vallist[i] == 1:
            handdict["Singles"].append(i) 

    # Evaluates if a hand contains a straight or not
    for i in range(len(val) - 1):
        if val[i] == val[i + 1] -1:
            if i == len(val) - 2:
                handdict["Straight"] = True
            else:
                continue
        
        # Deals with special case of aces
        else:
            if val == [2, 3, 4, 5, 14]:
                handdict["Straight"] = True
            break

    # Checks if the hand contains a flush
    if max(suits) == min(suits):
        handdict["Flush"] = True

    # Calculates the value for a hand using the dictionary
    
    if handdict["Flush"]:
        # Checks for straigh flushes
        if handdict["Straight"]:
            # Deal with special case for aces
            if val == [2, 3, 4, 5, 14]:
                return (8, 5)

            else:
                return (8, val[-1])

        else:
            # Only a flush
            return (5, val[-1])

    else:
        # Checks hand for a straight
        if handdict["Straight"]:
            # Deals with special case for aces
            if val == [2, 3, 4, 5, 14]:
                return (4, 5)

            else:
                return (4, val[-1])

        # Checks for 4 of a kind
        elif len(handdict["Fours"]) == 1:
            return (7, handdict["Fours"], max(handdict["Singles"]))

        # Checks for a 3 of a kind
        elif len(handdict["Threes"]) == 1:
            # Checks for full house
            if len(handdict["Pairs"]) == 1:
                return (6, handdict["Threes"], handdict["Pairs"])

            # Must be only 3 of a kind
            else:
                return (3, handdict["Threes"], max(handdict["Singles"]))

        # Checks for 2 pairs
        elif len(handdict["Pairs"]) == 2:
            return (2, max(handdict["Pairs"]), min(handdict["Pairs"]), 
                    handdict["Singles"])
        
        # Checks for a single pair
        elif len(handdict["Pairs"]) == 1:
            return (1, handdict["Pairs"], max(handdict["Singles"]))

        # Must be just a high card
        else:
            return (0, max(handdict["Singles"]))


def compare_hands(hand1, hand2):
    """
    Compares hands against each other and returns true if hand 1 wins
    """
    # Sets variable
    index = 0

    # Attempts to evaluate a winner from the hands
    # Starts with type of hand and then moves to tiebreakers 
    try:
        while True:
            if hand1[index] > hand2[index]:
                return True

            elif hand1[index] < hand2[index]:
                return False

            else:
                index += 1

    # If hand cant be resolved then an error message is printed along with the hand
    # Also returns False as a default
    except IndexError:
        print("Failed")
        print("{}\t{}".format(hand1, hand2))

        return False


# Calculates hands won only if program run as a script
if __name__ == '__main__':
    print(hands_won())
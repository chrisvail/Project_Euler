from random import randint

simlength = 100000
square_names = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
                "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
                "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
                "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

board  = [[square_names[i], i, 0] for i in range(len(square_names))]
position = 0
dice = [0, 0]
double_count = 0

for _ in range(simlength):
    dice = [randint(1, 4), randint(1, 4)]
    double_count = double_count + 1 if dice[0] == dice[0] else 0
    if double_count == 3:
        position = 10 # square_names.index("JAIL")

    else:

        position = (position + sum(dice)) % len(board)

        if position == 30: # square_names.index("G2J"):
            position = 10 # square_names.index("JAIL")
            
        elif square_names[position][:2] == "CC":
            chance = randint(1, 16)
            if chance == 1:
                position = 0 # square_names.index("GO")
            elif chance == 2:
                position = 10 # square_names.index("JAIL")

        elif square_names[position][:2] == "CH":
            chance = randint(1, 16)
            if chance == 1:
                position = 0 # square_names.index("GO")
            elif chance == 2:
                position = 10 # square_names.index("JAIL")
            elif chance == 3:
                position = 11 # square_names.index("C1")
            elif chance == 4:
                position = 24 # square_names.index("E3")
            elif chance == 5:
                position = 39 # square_names.index("H2")
            elif chance == 6:
                position = 5 # square_names.index("R1")
            elif chance == 7 or chance == 8:
                while square_names[position][:1] != "R":
                    position = (position + 1) % len(board)
            elif chance == 9:
                while square_names[position][:1] != "U":
                    position = (position + 1) % len(board)
            elif chance == 10:
                position -= 3

    board[position][2] += 1

board = sorted(board, key= lambda board: board[2])
for i in reversed(board[-3:]):
    if i[1] < 10:
        print("0{}".format(i[1]), end="")
    else:
        print(i[1], end="")
    
print()


boxes = [[0 for x in range(51)] for y in range(10000)]

boxes[1] = [1,1] + [0 for x in range(49)]

for i in range(2, 10000):
    boxes[i][0] = boxes[i - 1][0] + boxes[i - 1][-1]
    boxes[i][-1] = boxes[i - 1][-1] + boxes[i - 1][-2]

    for j in range(1, 50):
        boxes[i][j] = boxes[i - 1][j - 1]

    if boxes[i][0] + boxes[i][-1] > 1000000:
        print(i)
        break
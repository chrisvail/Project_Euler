

def main():
    
    boxes = [{"Black": 0, "OneRed": 0, "TwoRed": 0, "ThreePlusRed": 0} for _ in range(51)]

    boxes[1]["Black"] = 1
    boxes[1]["OneRed"] = 1

    for i in range(2, 51):

        boxes[i]["Black"] = boxes[i - 1]["Black"] + boxes[i - 1]["ThreePlusRed"]
        boxes[i]["OneRed"] = boxes[i - 1]["Black"]
        boxes[i]["TwoRed"] = boxes[i - 1]["OneRed"]
        boxes[i]["ThreePlusRed"] = boxes[i - 1]["TwoRed"] + boxes[i - 1]["ThreePlusRed"]

        print(i, boxes[i]["Black"] + boxes[i]["ThreePlusRed"])



if __name__ == '__main__':
    main()
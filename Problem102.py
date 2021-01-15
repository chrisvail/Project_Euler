from math import atan2, pi
from itertools import combinations

triangles = []

with open("Problem102.txt") as inpt:
    for line in inpt:
        coord = (line.strip('\n')).split(",")
        coord = [[int(coord[i]), int(coord[i + 1])] for i in range(0, 6, 2)]
        triangles.append(coord)

counter = 0

for tri in triangles:
    angles = []
    for point in tri:
        angle = atan2(point[1], point[0])
        if angle < 0:
            angle = (2 * pi) + angle

        angles.append(angle)

    angles = sorted(angles)
    #print(angles)
    difference = [angles[1] - angles[0], angles[2] - angles[1], angles[2] - angles[0]]
    if difference[0] < pi and difference[1] < pi and difference[2] > pi:
        counter += 1

print(counter)
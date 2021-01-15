from itertools import combinations

target = 50
points = [(x, y) for x in range(target + 1) for y in range(target + 1)]
points.remove((0, 0))
counter = 0

for point1, point2 in combinations(points, 2):
    lengths = [point1[0] ** 2 + point1[1] ** 2,
               point2[0] ** 2 + point2[1] ** 2, 
               (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2]

    a, b, c = sorted(lengths)
    if a + b == c:
        # print([point1, point2])
        counter += 1

        if counter % 1000 == 0:
            print("Counter at: {}".format(counter))

print(counter)
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def equals(self, point):
#         return self.x == point.x and self.y == point.y
def check_point(point):
    if point not in points_visited:
        points_visited.append(point)
    elif point not in points_visited_already:
        points_visited_already.append(point)


file = open('inputpuzzle5.txt', 'r')
filelines = file.read().splitlines()
points_visited = []
points_visited_already = []
for line in filelines:
    points = line.split(" -> ")
    point1 = (int(points[0].split(",")[0]), int(points[0].split(",")[1]))
    point2 = (int(points[1].split(",")[0]), int(points[1].split(",")[1]))
    if point1[0] == point2[0] or point1[1] == point2[1]:
        check_point(point1)
        check_point(point2)
        if point1[0] > point2[0]:
            for i in range(1, point1[0] - point2[0]):
                new_point = (point2[0] + i, point1[1])
                check_point(new_point)
        elif point1[0] < point2[0]:
            for i in range(1, point2[0] - point1[0]):
                new_point = (point1[0] + i, point1[1])
                check_point(new_point)
        elif point1[1] > point2[1]:
            for i in range(1, point1[1] - point2[1]):
                new_point = (point1[0], point2[1] + i)
                check_point(new_point)
        elif point1[1] < point2[1]:
            for i in range(1, point2[1] - point1[1]):
                new_point = (point1[0], point1[1] + i)
                check_point(new_point)
    elif abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
        check_point(point1)
        check_point(point2)
        if point1[0] > point2[0] and point1[1] > point2[1]:
            for i in range(1, point1[0] - point2[0]):
                new_point = (point2[0] + i, point2[1] + i)
                check_point(new_point)
        elif point2[0] > point1[0] and point2[1] > point1[1]:
            for i in range(1, point2[0] - point1[0]):
                new_point = (point1[0] + i, point1[1] + i)
                check_point(new_point)
        elif point1[0] < point2[0] and point1[1] > point2[1]:
            for i in range(1, point2[0] - point1[0]):
                new_point = (point1[0] + i, point1[1] - i)
                check_point(new_point)
        elif point1[0] > point2[0] and point1[1] < point2[1]:
            for i in range(1, point1[0] - point2[0]):
                new_point = (point1[0] - i, point1[1] + i)
                check_point(new_point)

print(len(points_visited_already))
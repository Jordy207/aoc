from collections import deque
import functools

file = open('inputpuzzle9.txt', 'r')
lines = file.read().splitlines()
down_len = len(lines)
width = len(lines[0])


def surrounding(input, x, y):
    vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]

mins = []
for row in range(down_len):
    for col in range(width):
        min_bool = True
        for (x_i, y_i) in surrounding(lines, row, col):
            if int(lines[row][col]) == 9 or int(lines[x_i][y_i]) < int(lines[row][col]):
                min_bool = False
        if min_bool:
            mins.append((row, col))

print(sum([int(lines[x][y]) + 1 for (x, y) in mins]))


def find_basins(input, x, y):
    print("finding basins")
    basin = []
    visited = []
    queue = deque([(x, y)])

    while queue:
        (x_i, y_i) = queue.pop()
        if (x_i, y_i) in visited:
            continue
        else:
            visited.append((x_i, y_i))
            if int(input[x_i][y_i]) != 9:
                basin.append((x_i, y_i))
                queue.extend([(x_j, y_j) for (x_j, y_j) in surrounding(input, x_i, y_i) if (x_j, y_j) not in visited])
    return basin

basins = [find_basins(lines, x, y) for (x, y) in mins]
top_basins = sorted([len(basin) for basin in basins], reverse=True)[0:3]
print(functools.reduce(lambda a, b: a*b, top_basins))
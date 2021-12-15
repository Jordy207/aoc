file = open('inputpuzzle11.txt', 'r')


def surrounding(input, x, y):
    vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]


flashes = 0

data = [[int(j) for j in list(line)] for line in file.read().splitlines()]
step = 0
while True:
    step += 1
    flashed = []
    neighbours = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 9:
                data[row][col] = 0
                flashes += 1
                flashed.append((row, col))
                neighbours.extend(surrounding(data, row, col))
            else:
                data[row][col] += 1
    while neighbours:
        ngb_row, ngb_col = neighbours.pop(0)
        if (ngb_row, ngb_col) not in flashed:
            if data[ngb_row][ngb_col] == 9:
                flashes += 1
                data[ngb_row][ngb_col] = 0
                if (ngb_row, ngb_col) not in flashed:
                    flashed.append((ngb_row, ngb_col))
                neighbours.extend(surrounding(data, ngb_row, ngb_col))
            else:
                data[ngb_row][ngb_col] += 1
    if step == 100:
        print(flashes)
    if len(flashed) == (len(data) * len(data[0])):
        print(step)
        break

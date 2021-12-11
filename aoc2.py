file1 = open('inputpuzzle2.txt', 'r')
lines = file1.readlines()

prev_line = float('inf')
horizontal = 0
depth = 0
aim = 0

for line in lines:
    if line.split()[0] == 'forward':
        horizontal += int(line.split()[1])
        depth += int(line.split()[1]) * aim
    if line.split()[0] == 'down':
        # depth += int(line.split()[1])
        aim += int(line.split()[1])
    if line.split()[0] == 'up':
        # depth += -int(line.split()[1])
        aim += -int(line.split()[1])

print(horizontal * depth)
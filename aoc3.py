from collections import Counter
from operator import itemgetter

file1 = open('inputpuzzle3.txt', 'r')
lines = file1.read().splitlines()

# Part 1
place_to_count = {}
for i in range(0, len(lines[0])):
    place_to_count[i] = Counter([x[i] for x in lines if len(x) > 0])

most = ""
least = ""

for i in range(0, len(lines[0])):
    most += place_to_count[i].most_common()[0][0]
    min_key, min_count = min(place_to_count[i] .items(), key=itemgetter(1))
    least += min_key

print(int(most, 2) * int(least, 2))


#  Part 2
current_lines_oxy = lines.copy()
current_lines_co2 = lines.copy()

position = 0
while len(current_lines_oxy) > 1:
    list_to_check = [int(x[position]) for x in current_lines_oxy]
    counter = Counter(list_to_check)
    item0 = 0
    item1 = 0
    for key in counter.keys():
        if key == 0:
            item0 = counter.get(key)
        if key == 1:
            item1 = counter.get(key)
    common_bit = 1
    if item0 > item1:
        common_bit = 0
    update_list = []
    for line in current_lines_oxy:
        if int(line[position]) == common_bit:
            update_list.append(line)
    position += 1
    current_lines_oxy = update_list


position = 0
while len(current_lines_co2) > 1:
    list_to_check = [int(x[position]) for x in current_lines_co2]
    counter = Counter(list_to_check)
    item0 = 0
    item1 = 0
    for key in counter.keys():
        if key == 0:
            item0 = counter.get(key)
        if key == 1:
            item1 = counter.get(key)
    common_bit = 0
    if item0 > item1:
        common_bit = 1
    update_list = []
    for line in current_lines_co2:
        if int(line[position]) == common_bit:
            update_list.append(line)
    position += 1
    current_lines_co2 = update_list

print(int(current_lines_oxy[0], 2) * int(current_lines_co2[0], 2))
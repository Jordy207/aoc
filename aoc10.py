from math import floor

file = open('inputpuzzle10.txt', 'r')
lines = file.read().splitlines()

openings = '{([<'
closings = '})]>'

closing = {cl: op for op, cl in zip(openings, closings)}
opening = {op: cl for op, cl in zip(openings, closings)}

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
auto_compl = {')': 1, ']': 2, '}': 3, '>': 4}

incompleted_lines = lines.copy()
error = 0
for line in lines:
    check_list = []
    for char in line:
        if char in openings:
            check_list.append(char)
        elif char in closings:
            if opening.get(check_list.pop()) != char:
                error += scores.get(char)
                incompleted_lines.remove(line)

print(error)

completion_scores = []

for line in incompleted_lines:
    score = 0
    check_list = []
    for char in line:
        if char in openings:
            check_list.append(char)
        elif char in closings:
            check_list.pop()
    while len(check_list) > 0:
        next_char = opening.get(check_list.pop())
        score = score * 5 + auto_compl.get(next_char)
    completion_scores.append(score)

print(sorted(completion_scores)[floor(len(completion_scores)/2)])
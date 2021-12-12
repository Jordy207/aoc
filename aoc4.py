class Board:

    def __init__(self, lines):
        self.lines = lines

    def print_board(self):
        print(self.lines)

    def check_win(self):
        for i in range(0, 5):
            row = [x[3] for x in self.lines if x[2] == i]
            if all(row):
                return self
        for i in range(0,5):
            column = [x[3] for x in self.lines if x[1] == i]
            if all(column):
                return self

    def set_entries(self, number_drawn):
        for item in self.lines:
            if item[0] == number_drawn:
                item[3] = True


file = open('inputpuzzle4.txt', 'r')
filelines = file.read().splitlines()
filelines = [value for value in filelines if value != '']
numbers = filelines[0]

board_list = []
board_lines = []
for idx, line in enumerate(filelines[1:]):
    if (idx % 5) != 4:
        for idx1, entry in enumerate(line.split()):
            board_lines.append([int(entry), idx1, idx % 5, False])
    else:
        for idx1, entry in enumerate(line.split()):
            board_lines.append([int(entry), idx1, idx % 5, False])
        board = Board(board_lines)
        board_list.append([board, False])
        board_lines = []
        row_counter = 0

win_board = None
winning_num = 0
for number in numbers.split(","):
    for board in board_list:
        board[0].set_entries(int(number))
        if board[0].check_win():
            win_board = board[0].check_win()
            winning_num = int(number)
    if win_board:
        break

winning_lines = win_board.lines
result = sum(x[0] for x in winning_lines if not x[3])
print(winning_num)
print(result)
print(result * winning_num)

last_board = None
last_num = None
for number in numbers.split(","):
    if len([x for x in board_list if not x[1]]) == 1:
        last_board = [x for x in board_list if not x[1]][0]
        last_num = int(number)
        last_board[0].set_entries(int(number))
        break
    for board in board_list:
        board[0].set_entries(int(number))
        if board[0].check_win():
            board[1] = True

losing_lines = last_board[0].lines
result = sum(x[0] for x in losing_lines if not x[3])
print(last_num)
print(result)
print(result * last_num)
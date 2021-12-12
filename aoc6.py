class Fishy:

    def __init__(self, days):
        self.days = days


file = open("inputpuzzle6.txt", 'r')
inputs = file.read()
# fishes = []
# for current in inputs:
#     fishes.append(Fishy(int(current)))
#
# for day in range(0, 256):
#     new_fish = []
#     for fish in fishes:
#         if fish.days == 0:
#             fish.days = 6
#             new_fish.append(Fishy(8))
#         else:
#             fish.days -= 1
#     fishes = fishes + new_fish
#
# print(len(fishes))

data = [inputs.count(str(i)) for i in range(9)]
for day in range(256):
    data[(day + 7) % 9] += data[day % 9]
    print(data)
print(sum(data))

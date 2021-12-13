file = open('inputpuzzle7.txt', 'r')
numbers = [int(number) for number in file.read().split(",")]

min_fuel = float('inf')

for number2 in range(min(numbers), max(numbers)+1):
    sum = 0
    for number in numbers:
        for i in range(1, abs(number2 - number) + 1):
            sum += i
    if sum < min_fuel:
        min_fuel = sum

print(min_fuel)
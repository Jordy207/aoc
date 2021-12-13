file = open('inputpuzzle8.txt', 'r')
lines = file.read().splitlines()

total_output = 0
for line in lines:
    line_input = line.split("|")[0].split()
    line_output = line.split("|")[1].split()
    signal_to_digit = {}
    unknown_digits = []
    for signal in line_input:
        if len(signal) == 2:
            signal_to_digit[1] = signal
        elif len(signal) == 3:
            signal_to_digit[7] = signal
        elif len(signal) == 4:
            signal_to_digit[4] = signal
        elif len(signal) == 7:
            signal_to_digit[8] = signal
        else:
            unknown_digits.append(signal)

    signal_to_loc = {'top': set(signal_to_digit[7]).difference(set(signal_to_digit[1]))}
    top_left_middle = set(signal_to_digit[4]).difference(set(signal_to_digit[1]))

    for unknown in unknown_digits:
        # 2 3 5
        if len(unknown) == 5:
            # finding 3
            if len(set(signal_to_digit[7]).intersection(set(unknown))) == 3:
                signal_to_digit[3] = unknown
            # finding 5
            elif len(top_left_middle.intersection(unknown)) == 2:
                signal_to_digit[5] = unknown
            # finding 2
            else:
                signal_to_digit[2] = unknown
        # 0 6 9
        else:
            # finding 9
            if len(set(unknown).intersection(set(signal_to_digit[4]))) == 4:
                signal_to_digit[9] = unknown
            # finding 6
            elif len(set(unknown).intersection(top_left_middle)) == 2:
                signal_to_digit[6] = unknown
            # finding 0
            else:
                signal_to_digit[0] = unknown

    signal_to_loc['middle'] = set(signal_to_digit[8]).difference(set(signal_to_digit[0]))
    signal_to_loc['bot_left'] = set(signal_to_digit[8]).difference(set(signal_to_digit[9]))
    signal_to_loc['top_right'] = set(signal_to_digit[8]).difference(set(signal_to_digit[6]))
    signal_to_loc['top_left'] = set(signal_to_digit[8]).difference(set(signal_to_digit[2]).union(set(signal_to_digit[3])))
    signal_to_loc['bot_right'] = set(signal_to_digit[8]).difference(set(signal_to_digit[2])).difference(signal_to_loc['top_left'])
    signal_to_loc['bottom'] = set(signal_to_digit[9]).difference(set(signal_to_digit[4]).union(set(signal_to_digit[7])))

    output = ''
    for signal in line_output:
        if len(signal) == 2:
            output += '1'
        elif len(signal) == 3:
            output += '7'
        elif len(signal) == 4:
            output += '4'
        elif len(signal) == 7:
            output += '8'
        else:
            if set(signal_to_digit[8]).difference(set(signal)) == signal_to_loc['bot_left']:
                output += '9'
            elif set(signal_to_digit[8]).difference(set(signal)) == signal_to_loc['top_right']:
                output += '6'
            elif set(signal_to_digit[8]).difference(set(signal)) == signal_to_loc['middle']:
                output += '0'
            elif set(signal_to_digit[8]).difference(set(signal)) == signal_to_loc['top_left'].union(signal_to_loc['bot_right']):
                output += '2'
            elif set(signal_to_digit[8]).difference(set(signal)) == signal_to_loc['top_left'].union(signal_to_loc['bot_left']):
                output += '3'
            else:
                output += '5'
    total_output += int(output)
print(total_output)

# part1
output_values = []
for line in lines:
    output_values += [output for output in line.split("|")[1].split()]

print(len([signal for signal in output_values if len(signal) in  [2,3,4,7]]))
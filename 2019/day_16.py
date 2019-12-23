import math


def create_pattern(base_pattern, repeats):

    new_pattern = []
    index = 0
    while index < len(base_pattern):
        for i in range(repeats):
            new_pattern.append(base_pattern[index])
        index += 1
    return new_pattern


# Get the input signal
input_signal = open('day_16.txt').read().strip()  # '69317163492948606335995924319873'
input_signal_list = [int(i) for i in input_signal]
print('initial')
print(input_signal_list, '\n')

# Define the base pattern
base_pattern = [0, 1, 0, -1]

# loop over the phases
for phase in range(100):
    print(phase)
    new_signal = []
    for repeats in range(1, len(input_signal)+1):
        # Get the required pattern for this round
        pattern = create_pattern(base_pattern, repeats)
        # print('repeats, pattern', repeats, pattern)

        # Make pattern the length of the input signal
        pattern_correct_length = pattern * (math.ceil((len(input_signal_list) / len(pattern))) + 1)
        pattern_correct_length = pattern_correct_length[1:len(input_signal_list)+1]

        # print('p', pattern_correct_length)

        # Multiply input signal by pattern element-wise
        new_signal.append(sum([x*y for x, y in zip(pattern_correct_length, input_signal_list)]))

    # Just use least significant character of int
    new_signal_reduced = [int(str(i)[-1]) for i in new_signal]
    input_signal_list = new_signal_reduced
    # print('s', input_signal_list)

print('\nfinal')
print(input_signal_list[:8])
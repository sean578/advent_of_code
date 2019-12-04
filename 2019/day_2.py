import numpy as np


def parse_program(program):

    index = 0

    # loop
    while index < program.shape[0]:

        add = None
        # read instruction, if halt then return
        if program[index] == 99:
            return program
        elif program[index] == 1:
            add = True
        elif program[index] == 2:
            add = False
        else:
            print('error, instruction not recognised')
            return

        # read the two input locations
        input_1_loc, input_2_loc = program[index + 1], program[index + 2]
        if add:
            output = program[input_1_loc] + program[input_2_loc]
        else:
            output = program[input_1_loc] * program[input_2_loc]

        # read the output location
        output_loc = program[index + 3]

        # perform the operation
        program[output_loc] = output

        # increment index
        index = index + 4

    return program


program = np.loadtxt('day_2.txt', delimiter=',', dtype=np.int32)

for noun in range(100):
    for verb in range(100):

        program_temp = np.copy(program)

        program_temp[1], program_temp[2] = noun, verb

        if parse_program(program_temp)[0] == 19690720:
            print(100*noun + verb)
            break

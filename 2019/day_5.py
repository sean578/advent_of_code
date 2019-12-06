import numpy as np


def parse_mode_opcode(instruction):
    instruct = str(instruction).zfill(5)
    opcode = int(instruct[-2:])
    modes = [int(x) for x in instruct[:-2]][::-1]
    return opcode, modes


def parse_program(program):

    # opcode:, params, inc
    inputs_params_incr = [
        [0, 0],
        [3, 4],
        [3, 4],
        [1, 2],
        [1, 2]
    ]

    index = 0
    while index < program.shape[0]:

        opcode, modes = parse_mode_opcode(program[index])

        # read instruction, if halt then return
        if opcode == 99:
            return program

        num_params, incr = inputs_params_incr[opcode]
        the_params = program[index+1:index+1+num_params]

        # print('############################# index = ', index)
        # print('opcode', opcode)
        # print('modes', modes)
        # print('num_params', num_params)
        # print('incr', incr)
        # print('the_params', the_params)

        if opcode == 1:
            program[the_params[2]] = (the_params[0] if modes[0] else program[the_params[0]]) +\
                                     (the_params[1] if modes[1] else program[the_params[1]])
        elif opcode == 2:
            program[the_params[2]] = (the_params[0] if modes[0] else program[the_params[0]]) *\
                                     (the_params[1] if modes[1] else program[the_params[1]])
        elif opcode == 3:
            program[the_params[0]] = np.int32(input("Enter input: "))
        elif opcode == 4:
            print((the_params[0] if modes[0] else program[the_params[0]]))
        else:
            print('error, instruction not recognised')
            return

        index = index + incr

    return program


program = np.loadtxt('day_5.txt', delimiter=',', dtype=np.int32)
parse_program(program)
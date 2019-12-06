import numpy as np


def parse_mode_opcode(instruction):
    instruct = str(instruction).zfill(5)
    opcode = int(instruct[-2:])
    modes = [int(x) for x in instruct[:-2]][::-1]
    return opcode, modes


def parse_program(program):

    # opcode:, params, inc
    num_params_lut = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    index = 0
    while index < program.shape[0]:

        opcode, modes = parse_mode_opcode(program[index])

        if opcode == 99:
            return program

        num_params = num_params_lut[opcode]
        the_params = program[index+1:index+1+num_params]

        increment = True
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
        elif opcode == 5:
            if (the_params[0] if modes[0] else program[the_params[0]]) != 0:
                increment = False
                index = the_params[1] if modes[1] else program[the_params[1]]
        elif opcode == 6:
            if (the_params[0] if modes[0] else program[the_params[0]]) == 0:
                increment = False
                index = the_params[1] if modes[1] else program[the_params[1]]
        elif opcode == 7:
            if (the_params[0] if modes[0] else program[the_params[0]]) < (the_params[1] if modes[1] else program[the_params[1]]):
                program[the_params[2]] = 1
            else:
                program[the_params[2]] = 0
        elif opcode == 8:
            if (the_params[0] if modes[0] else program[the_params[0]]) == (the_params[1] if modes[1] else program[the_params[1]]):
                program[the_params[2]] = 1
            else:
                program[the_params[2]] = 0
        else:
            print('error, instruction not recognised')
            return

        if increment:
            index = index + num_params+1

    return program


program = np.loadtxt('day_5.txt', delimiter=',', dtype=np.int32)
parse_program(program)
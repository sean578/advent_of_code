import numpy as np


def parse_mode_opcode(instruction):
    instruct = str(instruction).zfill(5)
    opcode = int(instruct[-2:])
    modes = [int(x) for x in instruct[:-2]][::-1]
    return opcode, modes


def parse_program(program, program_inputs):

    # opcode:, params, inc
    num_params_lut = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    index = 0
    input_index = 0
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
            program[the_params[0]] = program_inputs[input_index]  # np.int32(input("Enter input: "))
            input_index += 1
        elif opcode == 4:
            return the_params[0] if modes[0] else program[the_params[0]]
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

    return None


def run_combination(program, phase_settings):
    amp_output = 0
    for amp in range(5):
        amp_output = parse_program(program, [phase_settings[amp], amp_output])
    return amp_output


def valid_phase_generator():
    for i in range(44444+1):
        i_string = str(i).zfill(5)
        i_ints = [int(x) for x in i_string]
        if max(i_ints) <= 4:
            if len(i_string) == len(set(i_string)):
                yield i_ints


# example programs & phase settings
example_to_use = 2
example_programs = [
    np.array([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], dtype=np.int32),
    np.array([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], dtype=np.int32),
    np.array([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], dtype=np.int32)
]

valid_phase_gen = valid_phase_generator()

amp_out_max = 0
best_phase_settings = None
for phase_settings in valid_phase_gen:
    program = np.loadtxt('day_7.txt', delimiter=',', dtype=np.int32)
    # program = example_programs[example_to_use][:]
    amp_out = run_combination(program, phase_settings)
    # print(phase_settings, amp_out)
    if amp_out > amp_out_max:
        best_phase_settings = phase_settings
        amp_out_max = amp_out

print('Max amp out =', amp_out_max)
print('Best phase settings =', best_phase_settings)




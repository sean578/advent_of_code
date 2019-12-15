import numpy as np
import copy


def parse_mode_opcode(instruction):
    instruct = str(instruction).zfill(5)
    opcode = int(instruct[-2:])
    modes = [int(x) for x in instruct[:-2]][::-1]
    return opcode, modes


def command(mem, program_input, stop_on_input=False):
    """ Pass instructions until an input is required or an output is created
    """

    # opcode:, params, inc
    num_params_lut = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    output = None
    done_a_read = False
    while not output:

        increment = True

        opcode, modes = parse_mode_opcode(mem['memory'][mem['addr']])
        print(opcode, modes)
        if opcode == 99:
            return 99

        num_params = num_params_lut[opcode]
        param_vals = mem['memory'][mem['addr'] + 1: mem['addr'] + 1 + num_params]

        if opcode == 1:
            mem['memory'][param_vals[2]] = (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) + \
                                    (param_vals[1] if modes[1] else mem['memory'][param_vals[1]])
        elif opcode == 2:
            mem['memory'][param_vals[2]] = (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) * \
                                    (param_vals[1] if modes[1] else mem['memory'][param_vals[1]])
        elif opcode == 3:
            mem['memory'][param_vals[0]] = program_input
            if done_a_read and stop_on_input:
                return None
            done_a_read = True
        elif opcode == 4:
            output = param_vals[0] if modes[0] else mem['memory'][param_vals[0]]
        elif opcode == 5:
            if (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) != 0:
                increment = False
                mem['addr'] = param_vals[1] if modes[1] else mem['memory'][param_vals[1]]
        elif opcode == 6:
            if (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) == 0:
                increment = False
                mem['addr'] = param_vals[1] if modes[1] else mem['memory'][param_vals[1]]
        elif opcode == 7:
            if (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) < (
                    param_vals[1] if modes[1] else mem['memory'][param_vals[1]]):
                mem['memory'][param_vals[2]] = 1
            else:
                mem['memory'][param_vals[2]] = 0
        elif opcode == 8:
            if (param_vals[0] if modes[0] else mem['memory'][param_vals[0]]) == (
                    param_vals[1] if modes[1] else mem['memory'][param_vals[1]]):
                mem['memory'][param_vals[2]] = 1
            else:
                mem['memory'][param_vals[2]] = 0
        else:
            print('error, instruction not recognised')

        if increment:
            mem['addr'] = mem['addr'] + num_params + 1

    return output


def valid_phase_generator():
    for i in range(55555, 99999 + 1):
        i_string = str(i).zfill(5)
        i_ints = [int(x) for x in i_string]
        if max(i_ints) <= 9:
            if len(i_string) == len(set(i_string)):
                yield i_ints


# example memorys & phase settings
example_init_mems = [
    {
        'memory': np.array([
            3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5],
            dtype=np.int32),
        'addr': 0
    },
    {
        'memory': np.array([
            3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
            -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
            53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10],
            dtype=np.int32),
        'addr': 0
    },
    {
        'memory': np.loadtxt('day_7.txt', delimiter=',', dtype=np.int32),
        'addr': 0
    }

]

DEBUG = True
DEBUG_EXAMPLE = 2

phase_settings = [
    np.array([9, 8, 7, 6, 5], dtype=np.int32),
    np.array([9, 7, 8, 5, 6], dtype=np.int32)
]

valid_phase_gen = valid_phase_generator()
output_max = 0
for phase in valid_phase_gen:
    print(phase)

    # Create a separate memory for each amp (doesn't get reset)
    amp_mems = []
    for _ in range(5):
        if DEBUG:
            amp_mems.append(copy.deepcopy(example_init_mems[DEBUG_EXAMPLE]))
        else:
            amp_mems.append(np.loadtxt('day_7.txt', delimiter=',', dtype=np.int32))

    # Input phase for all amps
    for i in range(5):
        command(amp_mems[i], phase[i], stop_on_input=True)

    output, output_new = 0, 0
    pass_number = 0

    while output_new != 99:

        for i in range(5):
            output_new = command(amp_mems[i], output, stop_on_input=False)
            if output_new == 99:
                break
            output = output_new
        pass_number += 1

    #print('output', output)
    if output > output_max:
        output_max = output

print(output_max)

#
# for i in [0, 4]:
#     print('address amp0 =', amp_mems[i]['memory'])


import numpy as np
import copy


def parse_mode_opcode(instruction):
    instruct = str(instruction).zfill(5)
    opcode = int(instruct[-2:])
    modes = [int(x) for x in instruct[:-2]][::-1]
    return opcode, modes


def command(mem):
    """ Pass instructions until an input is required or an output is created
    """

    # opcode:, params, inc
    num_params_lut = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]

    while True:

        increment = True

        opcode, modes = parse_mode_opcode(mem['memory'][mem['addr']])
        if opcode == 99:
            return 99
        elif opcode > 9:
            return 'Fail'

        num_params = num_params_lut[opcode]
        param_vals_initial = mem['memory'][mem['addr'] + 1: mem['addr'] + 1 + num_params]
        param_vals = []

        # TODO: Simplify this logic
        for i in range(num_params):
            if i < 2:
                if modes[i] == 0:
                    param_vals.append(mem['memory'][param_vals_initial[i]])
                elif modes[i] == 1:
                    param_vals.append(param_vals_initial[i])
                elif modes[i] == 2:
                    if opcode == 3:
                        param_vals.append(param_vals_initial[i] + mem['relative_base'])
                    else:
                        param_vals.append(mem['memory'][param_vals_initial[i] + mem['relative_base']])
                else:
                    print('Wrong mode code')
            else:
                if modes[i] == 2:
                    param_vals.append(param_vals_initial[i] + mem['relative_base'])
                else:
                    param_vals.append(param_vals_initial[i])

        if opcode == 1:
            mem['memory'][param_vals[2]] = param_vals[0] + param_vals[1]
        elif opcode == 2:
            mem['memory'][param_vals[2]] = param_vals[0] * param_vals[1]
        elif opcode == 3:
            mem['memory'][param_vals[0]] = np.int64(input('Program input...'))
        elif opcode == 4:
            print(param_vals[0])
        elif opcode == 5:
            if param_vals[0] != 0:
                increment = False
                mem['addr'] = param_vals[1]
        elif opcode == 6:
            if param_vals[0] == 0:
                increment = False
                mem['addr'] = param_vals[1]
        elif opcode == 7:
            if param_vals[0] < param_vals[1]:
                mem['memory'][param_vals[2]] = 1
            else:
                mem['memory'][param_vals[2]] = 0
        elif opcode == 8:
            if param_vals[0] == param_vals[1]:
                mem['memory'][param_vals[2]] = 1
            else:
                mem['memory'][param_vals[2]] = 0
        elif opcode == 9:
            mem['relative_base'] += param_vals[0]
        else:
            print('error, instruction not recognised')

        if increment:
            mem['addr'] = mem['addr'] + num_params + 1


# example memorys & phase settings
example_init_mems = [
    {
        'memory': np.array([
            109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99
        ],
            dtype=np.int64),
        'addr': 0,
        'relative_base': 0
    },
    {
        'memory': np.array([
            1102, 34915192, 34915192, 7, 4, 7, 99, 0
        ],
            dtype=np.int64),
        'addr': 0,
        'relative_base': 0
    },
    {
        'memory': np.array([
            104, 1125899906842624, 99
        ],
            dtype=np.int64),
        'addr': 0,
        'relative_base': 0
    },
    {
        'memory': np.loadtxt('day_9.txt', delimiter=',', dtype=np.int64),
        'addr': 0,
        'relative_base': 0
    }

]

DEBUG = True
DEBUG_EXAMPLE = 3

zero_array = np.zeros((10000,), dtype=np.int32)
main_array = example_init_mems[DEBUG_EXAMPLE]['memory']

example_init_mems[DEBUG_EXAMPLE]['memory'] = np.concatenate([main_array, zero_array])

mems = copy.deepcopy(example_init_mems[DEBUG_EXAMPLE])
final_code = command(mems)

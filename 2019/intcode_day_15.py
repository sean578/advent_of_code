import numpy as np


class IntCode:

    def __init__(self, program_filename=None, DEBUG=False):
        if DEBUG:
            self.mem = np.zeros(10, dtype=np.int64)
        else:
            self.mem = np.loadtxt(program_filename, delimiter=',', dtype=np.int64)
        self.extend_memory()
        self.addr = 0
        self.rel_base = 0
        self.input_values = []
        self.output_values = []

    def extend_memory(self):
        zero_array = np.zeros((10000,), dtype=np.int64)
        self.mem = np.copy(np.concatenate([self.mem, zero_array]))

    def parse_mode_opcode(self, instruction):
        if instruction > 99999 or instruction < 0:
            raise Exception('Incorrect instruction found', instruction)
        instruct = str(instruction).zfill(5)
        opcode = int(instruct[-2:])
        modes = [int(x) for x in instruct[:-2]][::-1]
        if opcode < 0 or (opcode > 9 and opcode != 99):
            raise Exception('Incorrect opcode found:', opcode)
        for mode in modes:
            if mode > 2 or mode < 0:
                raise Exception('Incorrect mode found', mode)
        return opcode, modes

    def command(self):
        # opcode:, params, inc
        num_params_lut = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]

        while True:

            increment = True

            opcode, modes = self.parse_mode_opcode(self.mem[self.addr])
            # print(opcode, modes)
            if opcode == 99:
                self.output_values.append(99)
                return 'Program complete'
            elif opcode > 9:
                raise Exception('Incorrect opcode', opcode)

            num_params = num_params_lut[opcode]
            param_vals_initial = self.mem[self.addr + 1: self.addr + 1 + num_params]
            param_vals = []

            if len(param_vals_initial) != num_params:
                raise Exception('Wrong number of params for optode', num_parms)

            # TODO: Simplify this logic
            for i in range(num_params):
                if modes[i] == 0:  # Address mode
                    if opcode == 3 or i == 2:  # Provide address
                        param_vals.append(param_vals_initial[i])
                    else:
                        param_vals.append(self.mem[param_vals_initial[i]])
                elif modes[i] == 1:  # Value mode
                    if opcode == 3 or i == 2:
                        raise Exception('Input or add/plus to write found in value mode')
                    else:
                        param_vals.append(param_vals_initial[i])
                elif modes[i] == 2:  # Relative address mode
                    if opcode == 3 or i == 2:
                        param_vals.append(param_vals_initial[i] + self.rel_base)
                    else:
                        param_vals.append(self.mem[param_vals_initial[i] + self.rel_base])
                else:
                    raise Exception('Wrong mode code', modes[i])

            if opcode == 1:
                self.mem[param_vals[2]] = param_vals[0] + param_vals[1]
            elif opcode == 2:
                self.mem[param_vals[2]] = param_vals[0] * param_vals[1]
            elif opcode == 3:
                if len(self.input_values) == 0:
                    return 'require input'
                else:
                    self.mem[param_vals[0]] = self.input_values.pop(0)
            elif opcode == 4:
                self.output_values.append(param_vals[0])
            elif opcode == 5:
                if param_vals[0] != 0:
                    increment = False
                    self.addr = param_vals[1]
            elif opcode == 6:
                if param_vals[0] == 0:
                    increment = False
                    self.addr = param_vals[1]
            elif opcode == 7:
                if param_vals[0] < param_vals[1]:
                    self.mem[param_vals[2]] = 1
                else:
                    self.mem[param_vals[2]] = 0
            elif opcode == 8:
                if param_vals[0] == param_vals[1]:
                    self.mem[param_vals[2]] = 1
                else:
                    self.mem[param_vals[2]] = 0
            elif opcode == 9:
                self.rel_base += param_vals[0]
            else:
                raise Exception('error, instruction not recognised')

            if increment:
                self.addr = self.addr + num_params + 1

            # if opcode == 3:
            #     return 'Draw screen'

            # if opcode == 4:
            #     if len(self.output_values) == 0:
            #         raise Exception('Not outputting a value', self.output_values)
            #     else:
            #         return 'Output value'

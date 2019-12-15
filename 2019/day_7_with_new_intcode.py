from intcode_day_11 import IntCode


def valid_phase_generator(min_value, max_value):
    for i in range(min_value, max_value+1):
        i_string = str(i).zfill(5)
        i_ints = [int(x) for x in i_string]
        if max(i_ints) <= 4:
            if len(i_string) == len(set(i_string)):
                yield i_ints


def print_input_output_values(intcode_machines):
    print('Input/output values:')
    for amp in intcode_machines:
        print(amp.input_values, amp.output_values)


valid_phase_gen = valid_phase_generator(00000, 44444)

NUM_AMPS = 5
amp_out_max = 0
best_phase_settings = None
for phase_settings in valid_phase_gen:

    intcode_machines = []
    for amp in range(NUM_AMPS):
        intcode_machines.append(IntCode('day_7.txt'))
    # print(intcode_machines)

    for amp in range(NUM_AMPS):
        intcode_machines[amp].input_values.append(phase_settings[amp])

    intcode_machines[0].input_values.append(0)
    # print_input_output_values(intcode_machines)  ####################################

    intcode_machines[0].command()
    # print_input_output_values(intcode_machines)  ###################################

    for amp in range(1, NUM_AMPS):
        amp_out = intcode_machines[amp-1].output_values.pop(0)
        intcode_machines[amp].input_values.append(amp_out)
        intcode_machines[amp].command()

    amp_out = intcode_machines[4].output_values.pop(0)
    print(amp_out)

    if amp_out > amp_out_max:
        best_phase_settings = phase_settings
        amp_out_max = amp_out

print('Max amp out =', amp_out_max)
print('Best phase settings =', best_phase_settings)


from intcode_day_11 import IntCode

intcode = IntCode('day_9.txt')  # Initialise the program
intcode.input_values.append(2)  # Provide input value
intcode.command()

print(intcode.output_values)



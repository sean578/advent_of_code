from intcode_day_17 import IntCode


def print_scaffold_map(scaffold_map):
    print(''.join(scaffold_map))


program = IntCode('day_17.txt')

######################################################
# Define the program input commands
######################################################

main = [ord(i) for i in 'A,A,B,B,C,B,C,B,C,A\n']
move_1 = [ord(i) for i in 'L,10,L,10,R,6\n']
move_2 = [ord(i) for i in 'R,12,L,12,L,12\n']
move_3 = [ord(i) for i in 'L,6,L,10,R,12,R,12\n']
vid_feed = [ord(i) for i in 'n\n']

######################################################
# Input the commands
######################################################

program.command()
program.input_values.extend(main)  # Main movement routine list
program.command()
program.input_values.extend(move_1)  # First movement function
program.command()
program.input_values.extend(move_2)  # First movement function
program.command()
program.input_values.extend(move_3)  # First movement function
program.command()
program.input_values.extend([ord('n'), ord('\n')])  # Continuous video feed

print_scaffold_map(''.join(str(chr(x)) for x in program.output_values))
program.output_values = []

program.command()
print('answer', program.output_values[-2])
# print_scaffold_map(''.join(str(chr(x)) for x in program.output_values))

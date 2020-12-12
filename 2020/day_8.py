from util import load_input


def parse_line(line):
    a = line.strip('\n').split()
    a[1] = int(a[1])
    return a


def perform_instruction(instruction, address,  accum):
    operation, argument = instruction
    if operation == 'acc':
        accum += argument
        address += 1
    elif operation == 'jmp':
        address += argument
    elif operation == 'nop':
        address += 1
    else:
        print('Instruction not recognised')
    return address, accum


def play_program(program, address, accum):
    addresses_been = set()
    while address not in addresses_been:
        print(accum)
        addresses_been.add(address)
        address, accum = perform_instruction(program[address], address, accum)
    return address, accum

if __name__ == '__main__':
    filename = 'day_8.txt'
    program = load_input(filename, parse_line)

    # print('The program:')
    # for instruction in program:
    #     print(instruction)

    play_program(program, 0, 0)

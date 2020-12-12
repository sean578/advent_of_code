from util import load_input
from copy import deepcopy


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


def play_program(program, address, accum, final_address):
    addresses_been = set()
    while address not in addresses_been and address != final_address:
        addresses_been.add(address)
        address, accum = perform_instruction(program[address], address, accum)

    return address, accum, address == final_address


if __name__ == '__main__':
    filename = 'day_8.txt'
    program = load_input(filename, parse_line)
    final_address = len(program)

    # Also test without change the first adress?
    for i in range(final_address + 1):
        p = deepcopy(program)
        if p[i][0] == 'nop':
            p[i][0] = 'jmp'
        elif p[i][0] == 'jmp':
            p[i][0] = 'nop'

        _, accum, done = play_program(p, 0, 0, final_address)
        if done:
            break
    print('Part 2 answer:', accum)

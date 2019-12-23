from intcode_day_17 import IntCode
import numpy as np
import matplotlib.pyplot as plt


def print_scaffold_map(scaffold_map):
    print(''.join(scaffold_map))


def scaffold_map_array(scaffold_map):
    x_size = scaffold_map.index('\n')
    y_size = scaffold_map.count('\n')
    scaffold_map_no_line_returns = [ord(value) for value in scaffold_map if value != '\n']
    scaffold_map_numpy = np.reshape(np.array(scaffold_map_no_line_returns[:-1]), (y_size-1, x_size))
    plt.imshow(scaffold_map_numpy.astype(np.int8))
    plt.show()
    return scaffold_map_numpy


def find_intersections(scaffold_map):
    # Loop through elements, not the boarder
    num_intersections = 0
    intersection_coords = []
    for y in range(1, scaffold_map.shape[0]-1):
        for x in range(1, scaffold_map.shape[1]-1):
            if str(chr(scaffold_map[y, x])) == '#':
                if str(chr(scaffold_map[y+1, x])) == '#':
                    if str(chr(scaffold_map[y-1, x])) == '#':
                        if str(chr(scaffold_map[y, x+1])) == '#':
                            if str(chr(scaffold_map[y, x-1])) == '#':
                                num_intersections += 1
                                intersection_coords.append([y, x])

    print('num_intersections', num_intersections)
    return intersection_coords


def calculate_part_1_answer(coords):
    answer = 0
    for coord in coords:
        answer += coord[0]*coord[1]
    print('answer', answer)


program = IntCode('day_17.txt')
program.command()
scaffold_map = [chr(i) for i in program.output_values]
print_scaffold_map(scaffold_map)

scaffold_numpy = scaffold_map_array(scaffold_map)
intersetion_coords = find_intersections(scaffold_numpy)
calculate_part_1_answer(intersetion_coords)


wire_instructions_file = open('day_3.txt')

# Get the data into two lists as strings:
instructions = [None, None]
for i, wire in enumerate(wire_instructions_file.readlines()):
    instructions[i] = wire.strip().split(',')

# instructions[0] = ['R8','U5','L5','D3']
# instructions[1] = ['U7','R6','D4','L4']

# instructions[0] = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# instructions[1] = ['U62','R66','U55','R34','D71','R55','D58','R83']

# instructions[0] = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# instructions[1] = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']


def find_all_coords(instructions):
    """Loop through the instructions and append each new coordinate to a list
    """
    coords = []
    current_index = [0, 0]

    for instruction in instructions:
        num_moves = int(instruction[1:])

        if instruction[0] == 'R':
            for i in range(num_moves):
                coords.append([current_index[0]+i, current_index[1]])
            current_index = [current_index[0] + num_moves, current_index[1]]

        elif instruction[0] == 'D':
            for i in range(num_moves):
                coords.append([current_index[0], current_index[1]-i])
            current_index = [current_index[0], current_index[1] - num_moves]

        elif instruction[0] == 'U':
            for i in range(num_moves):
                coords.append([current_index[0], current_index[1]+i])
            current_index = [current_index[0], current_index[1] + num_moves]

        elif instruction[0] == 'L':
            for i in range(num_moves):
                coords.append([current_index[0]-i, current_index[1]])
            current_index = [current_index[0] - num_moves, current_index[1]]

        else:
            print('Incorrect direction encountered')
            break

    # add the final location
    coords.append(current_index)
    return coords


coords_0 = [tuple(x) for x in find_all_coords(instructions[0])]
coords_1 = [tuple(x) for x in find_all_coords(instructions[1])]
intersections = list(set(coords_0).intersection(coords_1))
print('Intersections\n', intersections)

man_dists = []
for intersection in intersections:
    man_dists.append(abs(intersection[0]) + abs(intersection[1]))

man_dists.remove(0) # Don't count an intersection at the origin

print('Min Manhattan distance\n', min(man_dists))

# Get the number of steps required for each intersection
# num steps is the index in coords

steps_for_intersections = []
for intersection in intersections:
    steps_for_intersections.append(coords_0.index(intersection) + coords_1.index(intersection))
steps_for_intersections.remove(0)

print('Min total steps\n', min(steps_for_intersections))
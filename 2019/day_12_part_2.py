import numpy as np
from itertools import combinations
import re
import math


def get_initial_positions(filename):
    positions_list = []
    for line in open(filename).readlines():
        line = list(map(int, re.findall(r'-?\d+', line)))
        positions_list.append(line)
    return np.array(positions_list, dtype=np.int32), np.zeros_like(positions_list)


def check_if_same_state(positions_initial, positions_now, velocities_initial, velocities_now):
    same = True
    for planet in range(positions_initial.shape[0]):
        if not np.array_equal(positions_initial[planet,:], positions_now[planet,:]):
            same = False
        if not np.array_equal(velocities_initial[planet,:], velocities_now[planet,:]):
            same = False
    return same


def check_if_same_state_1d(positions_initial, positions_now, velocities_initial, velocities_now, dimension):
    same = True
    for planet in range(positions_initial.shape[0]):
        if not np.array_equal(positions_initial[planet, dimension], positions_now[planet, dimension]):
            same = False
        if not np.array_equal(velocities_initial[planet, dimension], velocities_now[planet, dimension]):
            same = False
    return same


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


# [planet, position]
# [planet, velocity]
positions_initial, velocities_initial = get_initial_positions('day_12.txt')
positions, velocities = positions_initial.copy(), velocities_initial.copy()
planet_list = [0, 1, 2, 3]
planet_index_combs = list(combinations(planet_list, 2))
num_directions = 3
num_steps = [0, 0, 0]

same_state = False
for dir in range(num_directions):
    positions, velocities = positions_initial.copy(), velocities_initial.copy()
    while not same_state:
        num_steps[dir] += 1

        # Update the velocities
        for planet_comb in planet_index_combs:

            pos_0, pos_1 = positions[planet_comb[0], dir], positions[planet_comb[1], dir]
            vel_0, vel_1 = velocities[planet_comb[0], dir], velocities[planet_comb[1], dir]

            if pos_1 > pos_0:
                velocities[planet_comb[1], dir] -= 1
                velocities[planet_comb[0], dir] += 1
            elif pos_0 > pos_1:
                velocities[planet_comb[0], dir] -= 1
                velocities[planet_comb[1], dir] += 1

        # Update the positions
        for planet in planet_list:
            positions[planet, dir] += velocities[planet, dir]

        # Check if same state
        same_state = check_if_same_state_1d(positions_initial, positions, velocities_initial, velocities, dir)
        if same_state:
            same_state = False
            break

print(lcm(num_steps[0], lcm(num_steps[1], num_steps[2])))

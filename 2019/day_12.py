import numpy as np
from itertools import combinations
import re


def get_initial_positions(filename):
    positions_list = []
    for line in open(filename).readlines():
        line = list(map(int, re.findall(r'-?\d+', line)))
        positions_list.append(line)
    return np.array(positions_list, dtype=np.int32), np.zeros_like(positions_list)


def calculate_energies(planet_list, positions, velocities):
    e_pot = []
    e_kin = []
    for planet in planet_list:
        e_pot.append(np.sum(np.abs(positions[planet, :])))
        e_kin.append(np.sum(np.abs(velocities[planet, :])))
    e_tot = [i*j for i, j in zip(e_pot, e_kin)]
    return sum(e_tot)


# [planet, position]
# [planet, velocity]
positions, velocities = get_initial_positions('day_12.txt')
planet_list = [0, 1, 2, 3]
planet_index_combs = list(combinations(planet_list, 2))
num_iterations = 1000000
num_directions = 3

num_calcs = 0
num_crossings = [0, 0, 0]
for _ in range(num_iterations):
    for dir in range(num_directions):

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

            if pos_0 == pos_1:
                num_crossings += 1
            num_calcs += 1

        # Update the positions
        for planet in planet_list:
            positions[planet, dir] += velocities[planet, dir]

print('\nNum calcs, Num crossings', num_calcs, num_crossings)
print(num_calcs/num_crossings)

# Calculate energies
total_energy = calculate_energies(planet_list, positions, velocities)
print('\nTotal energy:', total_energy)



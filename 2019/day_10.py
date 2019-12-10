import numpy as np
from itertools import product
import math

a_map_string = []
f = open('day_10.txt').readlines()
for line in f:
    a_map_string.append([i for i in line.strip()])

a_map = (np.array(a_map_string) == '#').astype(int)
total_num_asteroids = np.sum(a_map)
y_max, x_max = a_map.shape
y_min, x_min = 0, 0

# Hold the number of asteroids that can be seen
num_asteroids_seen = np.zeros_like(a_map)

# Loop through all asteroids elements
for x, y in product(range(x_max), range(y_max)):
    if not a_map[y, x]:
        continue
    blocked = np.zeros(a_map.shape)  # An array to hold the blocked asteroids

    # Loop through all the positions relative to the host asteroid
    for X, Y in product(range(x_max), range(y_max)):
        # if there is not an asteroid then continue
        if not a_map[Y, X]:
            continue
        x_rel = X - x
        y_rel = Y - y
        if (x_rel == 0) and (y_rel == 0):
            continue

        # Loop through and check if blocked
        hcf = math.gcd(x_rel, y_rel)
        step_x = x_rel // hcf
        step_y = y_rel // hcf
        x_check = step_x + x_rel + x
        y_check = step_y + y_rel + y

        while(x_check >= x_min) \
                and (x_check < x_max) \
                and (y_check >= y_min) \
                and (y_check < y_max):

            if a_map[y_check, x_check]:
                blocked[x_check, y_check] = 1
            # multiplier += 1
            x_check += step_x
            y_check += step_y

    num_asteroids_seen[y, x] = int(total_num_asteroids - np.sum(blocked) - 1)

print(np.max(num_asteroids_seen))


import numpy as np
from itertools import product
import math

a_map_string = []
f = open('day_10.txt').readlines()
for line in f:
    a_map_string.append([i for i in line.strip()])

a_map = (np.array(a_map_string) == '#').astype(int)
y_max, x_max = a_map.shape


def get_asteroid_coords(a_map, x_max, y_max):
    coord_list = []
    for x, y in product(range(x_max), range(y_max)):
        if a_map[y, x]:
            coord_list.append([y, x])
    return coord_list


def get_rel_coord_list(coord_list, home_y, home_x):
    coord_list_rel = []
    for coord in coord_list:
        if coord != [home_y, home_x]:
            coord_list_rel.append([coord[0] - home_y, coord[1] - home_x])
    return coord_list_rel


def get_angle_distance_lists(coord_list_rel):
    coord_list_angle = []
    coord_list_distance = []
    for coord in coord_list_rel:

        theta = math.degrees(math.atan2(coord[0], coord[1]))
        if theta < 0:
            theta += 360.0
        coord_list_angle.append(theta)
        coord_list_distance.append(math.sqrt(coord[0]**2 + coord[1]**2))
    return coord_list_angle, coord_list_distance


home = (28, 29)

coord_list = get_asteroid_coords(a_map, x_max, y_max)
coord_list_rel = get_rel_coord_list(coord_list, *home)
coord_list_angle, coord_list_distance = get_angle_distance_lists(coord_list_rel)

the_200th = None
num_destroyed = 1
inc = 1e-6
laser_angle = 270
while len(coord_list_rel) > 0:
    asteroids_n_path = [i for i in coord_list_angle if i >= laser_angle]
    if len(asteroids_n_path) == 0:
        laser_angle = 0
        continue
    min_angle = min(asteroids_n_path)
    laser_angle = min_angle+inc
    list_candidate_asteroids = [i for i, n in enumerate(coord_list_angle) if n == min_angle]

    # find closest asteroid
    distances = []
    for index in list_candidate_asteroids:
        distances.append(coord_list_distance[index])
    closest = list_candidate_asteroids[distances.index(min(distances))]
    absolute = [coord_list_rel[closest][1] + home[1], coord_list_rel[closest][0] + home[0]]
    # print(num_destroyed, absolute)
    if num_destroyed == 200:
        the_200th = absolute
    num_destroyed += 1

    # remove asteroids from lists
    coord_list_rel.pop(closest)
    coord_list_angle.pop(closest)
    coord_list_distance.pop(closest)

print('200th asteroid coords =', the_200th)
print('Question answer =', the_200th[0]*100 + the_200th[1])

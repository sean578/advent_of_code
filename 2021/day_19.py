import scipy.spatial.transform
from scipy.spatial.distance import cdist
import numpy as np
import copy


def read_data(filename):
    lines = [line.strip() for line in open(filename).readlines()]

    scans = {}

    scanner_number = -1
    first = False
    for line in lines:
        if line[:3] == '---':
            scanner_number += 1
            first = True
        elif line == '':
            pass
        else:
            beacon_as_list = [int(i) for i in line.split(',')]
            if first:
                first = False
                scans[scanner_number] = np.array(beacon_as_list, np.int16)
            else:
                scans[scanner_number] = np.vstack((scans[scanner_number], np.array(beacon_as_list, np.int16)))

    return scans


def rotate_vectors(beacons, num_rotations, rotation_group):
    # Beacons shape: # beacons * 3 coords

    # If no rotation to be done, return original matrix
    if num_rotations == 0:
        return beacons

    # Wrap around so number of rotations is less than 24
    while num_rotations > 24:
        num_rotations = num_rotations % 24

    # Do the transformation
    return (beacons @ rotation_group[num_rotations - 1]).astype(np.int16)


if __name__ == '__main__':
    scans = read_data('day_19.txt')
    num_scanners = len(scans)
    print('Number of scanners:', num_scanners)

    translations_to_abs = {key: None for key in scans}
    translations_to_abs[0] = np.array([0, 0, 0])  # Scanner 0 already in absolute coords

    rotations_to_abs = {key: None for key in scans}
    rotations_to_abs[0] = 0
    rotation_group = scipy.spatial.transform.Rotation.create_group('O').as_matrix()

    scans_done = {0: copy.deepcopy(scans[0])}

    while len(scans_done) < num_scanners:
        print('Number of scanners done:', len(scans_done.keys()))
        to_try = tuple(scans_done.keys())
        for done_number in to_try:
            for i, beacon_abs in enumerate(scans_done[done_number]):
                x = set([tuple(i) for i in scans_done[done_number]])
                for scanner_number in range(1, num_scanners):
                    if scanner_number not in scans_done:
                        for num_rotations in range(25):
                            beacons = copy.deepcopy(scans[scanner_number])
                            beacons_rotated = rotate_vectors(beacons, num_rotations, rotation_group)
                            for j, beacon_rel in enumerate(beacons_rotated):
                                translation = beacon_abs - beacon_rel
                                beacon_in_abs = beacons_rotated + translation
                                y = set([tuple(i) for i in beacon_in_abs])
                                num_overlap = len(x.intersection(y))
                                if num_overlap >= 12:
                                    translations_to_abs[scanner_number] = translation  # The translation required, after rotation has been applied
                                    rotations_to_abs[scanner_number] = num_rotations
                                    scans_done[scanner_number] = beacon_in_abs  # Apply the rotation then translation here
                                    break

    # Part 1 answer
    the_beacons = set()
    for scanner in scans_done.values():
        for beacon in scanner:
            the_beacons.add(tuple(beacon))
    print('Answer part 1:', len(the_beacons))

    # Part 2 answer
    print(translations_to_abs)
    save_filename = 'day_19_part_1_result.npy'
    np.save(save_filename, translations_to_abs, allow_pickle=True)

    sp = np.load('/home/sean/Documents/repos/advent_of_code/2021/day_19_part_1_result.npy', allow_pickle=True)

    x = sp.item().values()
    max_manhattan = 0
    for a in x:
        for b in x:
            man = np.sum(np.abs(a - b))
        if man > max_manhattan:
            max_manhattan = man
    print('Max manhattan distance:', max_manhattan)
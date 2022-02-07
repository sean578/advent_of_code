from collections import defaultdict
import numpy as np
import copy


def read_data(filename):
    lines = [line.strip() for line in open(filename).readlines()]

    scans = defaultdict(list)

    scanner_number = -1
    for line in lines:
        if line[:3] == '---':
            scanner_number += 1
        elif line == '':
            pass
        else:
            scans[scanner_number].append(np.array([int(i) for i in line.split(',')], np.int16))

    return scans


def roll(v, dir):
    if dir == 'R':
        return v[0], v[2], -v[1]
    elif dir == 'T':
        return -v[1], v[0], v[2]
    else:
        print('Incorrect direction')


def rotate_vector(vector, num_rotations):

    v = copy.deepcopy(vector)

    a = 'RTTTRTTTRTTT'
    turn_around = 'RTR'

    if num_rotations == 0:
        return v
    elif num_rotations <= 12:
        for i in range(num_rotations):
            v = roll(v, a[i])
    else:
        for r in a:
            v = roll(v, r)
        for r in turn_around:
            v = roll(v, r)
        for i in range(num_rotations % 12):
            v = roll(v, a[i])

    return v


if __name__ == '__main__':
    scans = read_data('day_19_test.txt')
    print('Input data:')
    for scanner, beacons in scans.items():
        print(scanner, beacons)

    # For scanner 2:
        # Set absolute position such that a beacon line up
        # Transform all coords into absolute and check overlap - are there 12 beacons
        # If 12 beacons found, calc absolute position of scanner 2. Else...
        # Do rotation of all coords and try again
        # If out of rotations finish and move on to next scanner

    # for scanner 1..n while all overlaps not found
    for num_rotations in range(24):

        for i, beacon_abs in enumerate(scans[0]):
            for j, beacon_rel in enumerate(scans[1]):
                # Rotate beacon
                beacon_rel = rotate_vector(beacon_rel, num_rotations)
                # Find transformation such that the two beacons overlap
                translation = beacon_abs - beacon_rel
                # print('Translation', translation)
                # Transform into abs coords
                beacon_in_abs = [tuple(rotate_vector(beacon, num_rotations) + translation) for beacon in scans[1]]
                orig = [tuple(b) for b in scans[0]]
                # print('Beacon in abs', beacon_in_abs)
                num_overlap = len(set(orig).intersection(set(beacon_in_abs)))
                if num_overlap > 1:
                    print('Translation', translation)
                    print(num_rotations, i, j, num_overlap)


    # Keep going checking against scanners whose absolute position is known until all scanner positions known

    # Complexity:
    # n^2 where n = number of scanners
    # 24 rotations
    # 25*25 = 625 beacons to overlap
    # 25 checks for overlap
    # 900 * 24 * 625 * 25 = 300e6 calcs


from collections import defaultdict
import numpy as np
import copy


def read_data(filename):
    lines = [line.strip() for line in open(filename).readlines()]

    scans = defaultdict(None)

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


def rotate(v, dir):
    if dir == 'R':
        return v @ np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    elif dir == 'T':
        return v @ np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    else:
        print('Incorrect direction:', dir)


def rotate_vectors(beacons, num_rotations):

    a = 'RTTTRTTTRTTT'
    turn_around = 'RTR'

    if num_rotations == -1:
        return beacons
    elif num_rotations < 12:
        beacons = rotate(beacons, a[num_rotations])
    elif num_rotations == 12:
        for i in turn_around:
            beacons = rotate(beacons, i)
        beacons = rotate(beacons, a[num_rotations % 12])
    else:
        beacons = rotate(beacons, a[num_rotations % 12])

    return beacons


if __name__ == '__main__':
    scans = read_data('day_19_test.txt')

    # for scanner 1..n while all overlaps not found

    for i, beacon_abs in enumerate(scans[0]):
        beacons_rotated = copy.deepcopy(scans[1])
        for num_rotations in range(24):
            beacons_rotated = rotate_vectors(beacons_rotated, num_rotations)
            x = set([tuple(i) for i in scans[0]])
            for j, beacon_rel in enumerate(beacons_rotated):
                # Find transformation such that the two beacons overlap
                translation = beacon_abs - beacon_rel
                # Transform into abs coords
                beacon_in_abs = beacons_rotated + translation
                # TODO: Find a numpy way to do the number of common rows to speed up...
                y = set([tuple(i) for i in beacon_in_abs])
                num_overlap = len(x.intersection(y))
                if num_overlap == 12:
                    print('Translation', translation)
                    print(num_rotations, i, j, num_overlap)


    # Keep going checking against scanners whose absolute position is known until all scanner positions known

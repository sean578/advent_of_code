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
    num_scanners = len(scans)
    print('Number of scanners:', num_scanners)

    translations_to_abs = {key: None for key in scans}
    translations_to_abs[0] = np.array([0, 0, 0])  # Scanner 0 already in absolute coords

    rotations_to_abs = {key: None for key in scans}
    rotations_to_abs[0] = 0

    scans_done = {0}
    while len(scans_done) < num_scanners:
        print('Scanners done progress:', scans_done)
        for done_number in copy.deepcopy(scans_done):
            for i, beacon_abs in enumerate(scans[done_number]):
                x = set([tuple(i) for i in scans[done_number]])
                for scanner_number in range(1, num_scanners):
                    if scanner_number not in scans_done:
                        beacons_rotated = copy.deepcopy(scans[scanner_number])
                        for num_rotations in range(24):
                            beacons_rotated = rotate_vectors(beacons_rotated, num_rotations)
                            for j, beacon_rel in enumerate(beacons_rotated):
                                # Find transformation such that the two beacons overlap
                                translation = beacon_abs - beacon_rel
                                # Transform into abs coords
                                beacon_in_abs = beacons_rotated + translation
                                # TODO: Find a numpy way to do the number of common rows to speed up...
                                y = set([tuple(i) for i in beacon_in_abs])
                                num_overlap = len(x.intersection(y))
                                if num_overlap == 12:
                                    translations_to_abs[scanner_number] = translation
                                    rotations_to_abs[scanner_number] = num_rotations
                                    scans_done.add(scanner_number)
                                    break

    print('Scans done:', scans_done)
    print('Translations to abs:', translations_to_abs)
    print('Rotations to abs:', rotations_to_abs)



    # TODO: Use translations & rotations found to convert all beacons to absolute coords and add to set
    # TODO: Answer for part 1 is the length of that set

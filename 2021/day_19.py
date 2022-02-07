import scipy.spatial.transform
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
    scans = read_data('day_19_test.txt')

    # for scanner 1..n while all overlaps not found
    num_scanners = len(scans)
    print('Number of scanners:', num_scanners)

    translations_to_abs = {key: None for key in scans}
    translations_to_abs[0] = np.array([0, 0, 0])  # Scanner 0 already in absolute coords

    rotations_to_abs = {key: None for key in scans}
    rotations_to_abs[0] = 0
    rotation_group = scipy.spatial.transform.Rotation.create_group('O').as_matrix()

    scans_done = {0}
    while len(scans_done) < num_scanners:
        print('Scanners done progress:', scans_done)
        for done_number in copy.deepcopy(scans_done):
            for i, beacon_abs in enumerate(scans[done_number]):
                x = set([tuple(i) for i in scans[done_number]])
                for scanner_number in range(1, num_scanners):
                    if scanner_number not in scans_done:
                        for num_rotations in range(24):
                            beacons = copy.deepcopy(scans[scanner_number])
                            beacons_rotated = rotate_vectors(beacons, num_rotations, rotation_group)
                            # beacons_rotated = rotate_vectors(beacons_rotated, num_rotations)
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

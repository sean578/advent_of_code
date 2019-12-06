def get_pairs_into_dict(debug=False, debug_array = None):
    orbit_dict = {}
    if debug:
        for line in debug_array:
            a, b = line.split(')')
            if b not in orbit_dict.keys():
                orbit_dict[b] = a
            else:
                print('Duplicate orbit found')
    else:
        for line in open('day_6.txt').readlines():
            a, b = line.strip().split(')')
            if b not in orbit_dict.keys():
                orbit_dict[b] = a
            else:
                print('Duplicate orbit found')

    return orbit_dict

# Simple input shown in question, distance between you and santa = 4
debug_array = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)YOU',
    'I)SAN'
]


def find_distance_to_com_recursive(planet, orbit_dict, dist=0):
    """ Recursive version of function used for part a
    """

    new_planet = orbit_dict[planet]
    if new_planet == 'COM':
        return dist + 1
    else:
        dist = find_distance_to_com_recursive(new_planet, orbit_dict, dist+1)
    return dist


def get_list_of_orbits_to_com(planet, orbit_dict):
    orbit_list = [planet]
    p = planet
    done = False
    while not done:
        p = orbit_dict[p]
        orbit_list.append(p)
        if p == 'COM':
            done = True
    return orbit_list


# Get in form, b orbits a --> [b] = a
orbit_dict = get_pairs_into_dict(debug=False, debug_array=debug_array)

# Get path through orbits to com for both you and santa
you_orbits = get_list_of_orbits_to_com('YOU', orbit_dict)
san_orbits = get_list_of_orbits_to_com('SAN', orbit_dict)

# Find the first intersection in these paths
intersections = set(you_orbits).intersection(san_orbits)

# Calc the distance between you and santa via the intersection and find the min
min_distance = min([you_orbits.index(x) + san_orbits.index(x) - 2 for x in intersections])
print('Min distance between you and santa =', min_distance)
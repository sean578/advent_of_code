def get_pairs_into_dict(debug=False, debug_array = None):
    orbit_dict = {}
    if debug:
        print(debug_array)
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
    'K)L'
]


def find_distance_to_com(planet, orbit_dict):
    count_orbits = 0
    p = planet
    done = False
    while not done:
        p = orbit_dict[p]
        count_orbits += 1
        if p == 'COM':
            done = True
    return count_orbits


# Get in form, b orbits a --> [b] = a
# orbit_dict = get_pairs_into_dict()
orbit_dict = get_pairs_into_dict(debug=False, debug_array=debug_array)

print(orbit_dict)
# print(find_distance_to_com('L', orbit_dict))

# Dictionary to store the number of orbits to get to COM
distance_to_com = dict.fromkeys(orbit_dict, 0)

# loop through keys to get num orbits linked to COM
total_orbits = 0
for planet in distance_to_com.keys():
    distance_to_com[planet] = find_distance_to_com(planet, orbit_dict)
    total_orbits += distance_to_com[planet]

print(total_orbits)


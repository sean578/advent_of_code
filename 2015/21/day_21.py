import itertools


def apply_rings(params, ring_list):

    # If no rings then parameters don't change
    if len(ring_list) == 0:
        return params

    ring_cost = 0

    for ring in ring_list:
        params['damage'] = params['damage'] + ring[1]
        params['armor'] = params['armor'] + ring[2]
        ring_cost = ring_cost + ring[0]

    return params, ring_cost


def who_wins(a_params, b_params):
    """
    :param a_params: Dictionary of parameters for you
    :param b_params: Dictionary of parameters for boss
    :return: String providing winner 'a' or 'b'
    """

    # Check if hit points are already zero or less
    if b_params['hit'] <= 0:
        return 'boss starting dead'
    if a_params['hit'] <= 0:
        return 'you starting dead'

    while True:
        b_params['hit'] = b_params['hit'] - (a_params['damage'] - b_params['armor'])
        if b_params['hit'] <= 0:
            return 'a'
        a_params['hit'] = a_params['hit'] - (b_params['damage'] - a_params['armor'])
        if a_params['hit'] <= 0:
            return 'b'


# cost, damage, armor
weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armor = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

# hit points for both you and the boss
hit = 100

max_cost = 0

# loop over item combinations here
for num_rings in range(3):
    for rings_current in itertools.combinations(rings, num_rings):
        for weapon_current in weapons:
            for armor_current in armor:

                # create stats based on weapon & armor & hit points
                you = {
                    'hit': hit,
                    'damage': weapon_current[1],
                    'armor': armor_current[2]
                }

                # define the boss parameters
                boss = {
                    'hit': hit,
                    'damage': 8,
                    'armor': 2
                }

                # Get total cost of weapon + armor
                cost = weapon_current[0] + armor_current[0]

                # apply rings
                if num_rings == 0:
                    you_with_rings, price_of_rings = you, 0
                else:
                    you_with_rings, price_of_rings = apply_rings(you, rings_current)
                cost = cost + price_of_rings

                if who_wins(you_with_rings, boss) == 'b':
                    if cost > max_cost:
                        max_cost = cost

print('\nMAX COST =', max_cost)

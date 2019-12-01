import itertools as iter

"""
Least amount of mana and still win?
"""

# TODO: Try using Spinx with this.


def who_wins(you_points, boss_points, magic_dict, magic_index, magic_sequence):
    """
    :param you_points: Dictionary of 'Hit' and 'Mana for you
    :param boss_points: Dictionary of 'Hit' and 'Damage' for the boss
    :param magic_dict: What each magic type does.
    :param magic_index: Defines the arrays of the magic
    :param magic_sequence: The sequence of spells to cast
    :return: who wins - you, 'y' or the boss, 'b'
    """

    # spell_name, num_turns_left
    active_spell_list = []  # Keep track of which spells are active

    magic_sequence_index = 0
    both_alive = True
    while both_alive:  # Will keep repeating sequence until someone loses

        # print('\n-- Player turn --')
        # print_scores(you_points, boss_points)

        if magic_sequence_index >= len(magic_sequence):
            return 'ERROR: Run out of spells'

        magic_name = magic_sequence[magic_sequence_index]
        spell_to_cast = magic_dict[magic_name]
        # print('Player casts {}'.format(magic_name))

        # reduce mana from applying spell
        reduce_mana(you_points, spell_to_cast[magic_index['MANA_COST']])

        # if mana run out return
        if mana_run_out(you_points):
            return 'b'

        # TODO: Fit this in better
        if magic_name == 'Shield':
            you_points['Armor'] = 7
            # print('Applied shield ###############')
            # print('\n####### Armor now 7 #########\n')

        # loop through active list and apply spells
        # go through active spell list & reduce # turns, remove any spells that become inactive
        active_spell_list = apply_spells(active_spell_list, you_points, boss_points)

        # if spell occurs instantly, apply it now        print('before spells applied...')
        if spell_to_cast[magic_index['TURNS']] == 0:
            boss_points['Hit'] = boss_points['Hit'] - spell_to_cast[magic_index['DAMAGE']]  # apply the spell damage
            if spell_to_cast[magic_index['HEALS']] > 0:
                you_points['Hit'] = you_points['Hit'] + spell_to_cast[magic_index['HEALS']]  # apply any healing
        else:  # Otherwise add it to the list of active spells (will be applied next turn)
            # TODO: Check spell isn't already active (or leave to outer script?)
            already_active = False
            for spell in active_spell_list:
                if spell[0] == magic_name:
                    already_active = True
            if not already_active:
                active_spell_list.append([magic_name, spell_to_cast[magic_index['TURNS']]])

        # check if boss is dead
        if is_person_dead(boss_points):
            return 'y'

        # print('\n-- Boss turn --')
        # print_scores(you_points, boss_points)

        # do boss's turn...
        # 1) loop through active list and apply spells
        active_spell_list = apply_spells(active_spell_list, you_points, boss_points)
        # check if boss is dead
        if is_person_dead(boss_points):
            return 'y'
        # 3) apply damage from boss
        apply_damage_from_boss(you_points, boss_points)
        # check if you are dead
        if is_person_dead(you_points):
            return 'b'

        magic_sequence_index = magic_sequence_index + 1


def apply_spells(spell_list, you_points, boss_points):
    name = 0
    turns = 1

    spell_list_updated = []
    for spell in spell_list:

        if spell[turns] > 0:
            spell_list_updated.append(spell)
            spell_list_updated[-1][turns] = spell_list_updated[-1][turns] - 1

    shield_in_list = False
    for spell in spell_list_updated:
        # print('Applying', spell[name])
        # TODO: Get rid of these magic numbers
        if spell[name] == 'Shield':
            shield_in_list = True
        elif spell[name] == 'Poison':
            boss_points['Hit'] = boss_points['Hit'] - 3
        elif spell[name] == 'Recharge':
            you_points['Mana'] = you_points['Mana'] + 101

    if shield_in_list:
        you_points['Armor'] = 7
    else:
        you_points['Armor'] = 0

    return spell_list_updated


def apply_damage_from_boss(you_points, boss_points):
    you_points['Hit'] = you_points['Hit'] - (boss_points['Damage'] - you_points['Armor'])


def is_person_dead(points):

    if points['Hit'] <= 0:
        return True
    else:
        return False


def mana_run_out(points):

    if points['Mana'] <= 0:
        return True
    else:
        return False


def reduce_mana(points, cost):

    points['Mana'] = points['Mana'] - cost
    return points


def print_scores(you_points, boss_points):

    # TODO: Use logger rather than print statements
    print('Player has {} hit points, {} armor, {} mana'.format(you_points['Hit'], you_points['Armor'], you_points['Mana']))
    print('Boss has {} hit points'.format(boss_points['Hit']))


boss = {
    'Hit': 55,
    'Damage': 8
}

you = {
    'Hit': 50,
    'Armor': 0,
    'Mana': 500
}

index = {
    'MANA_COST': 0,
    'DAMAGE': 1,
    'HEALS': 2,
    'ARMOR': 3,
    'TURNS': 4,
    'MANA_GAIN': 5
}

# Mana, damage, heals, armor, turns, mana gain
magic = {
    'Magic Missile': [53, 4, 0, 0, 0, 0],
    'Drain': [73, 2, 2, 0, 0, 0],
    'Shield': [113, 0, 0, 7, 6, 0],
    'Poison': [173, 3, 0, 0, 6, 0],
    'Recharge': [229, 0, 0, 0, 5, 101]
}

if __name__ == '__main__':

    sequences = iter.product([
        'Magic Missile',
        'Drain',
        'Shield',
        'Poison',
        'Recharge'], repeat = 5
    )

    test_sequence_1 = ['Poison', 'Magic Missile']
    test_sequence_2 = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']

    # winner = who_wins(you, boss, magic, index, test_sequence_1)
    # print(winner)

    min_mana = 999999999
    for sequence in sequences:

        boss = {
            'Hit': 55,
            'Damage': 8
        }

        you = {
            'Hit': 50,
            'Armor': 0,
            'Mana': 500
        }

        # TODO: Output amount of mana spent to win fight (clarify amount)
        winner = who_wins(you, boss, magic, index, sequence)
        if winner == 'y':
            print(sequence)


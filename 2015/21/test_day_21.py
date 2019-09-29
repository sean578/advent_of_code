import pytest
import day_21


def test_apply_rings():

    you_in = {
        'hit': 100,
        'damage': 0,
        'armor': 0
    }

    you_out = {
        'hit': 100,
        'damage': 1,
        'armor': 3
    }

    rings = [(25, 1, 3)]

    assert day_21.apply_rings(you_in, rings)[0] == you_out
    assert day_21.apply_rings(you_in, rings)[1] == 25


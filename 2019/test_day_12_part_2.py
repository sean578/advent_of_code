import numpy as np
from day_12_part_2 import check_if_same_state, check_if_same_state_1d


def test_check_if_same_state():
    num_planets = 4
    num_directions = 3
    assert check_if_same_state(np.zeros((num_planets, num_directions), dtype=np.int32),
                               np.zeros((num_planets, num_directions), dtype=np.int32),
                               np.zeros((num_planets, num_directions), dtype=np.int32),
                               np.zeros((num_planets, num_directions), dtype=np.int32)
                               ) is True

    test_array_1 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [-10, -11, 5]], dtype=np.int32)
    test_array_2 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [-10, -12, 5]], dtype=np.int32)

    assert check_if_same_state(test_array_1,
                               test_array_1,
                               test_array_1,
                               test_array_1
                               ) is True

    assert check_if_same_state(test_array_1,
                               test_array_1,
                               test_array_2,
                               test_array_2
                               ) is True

    assert check_if_same_state(test_array_1,
                               test_array_2,
                               test_array_2,
                               test_array_2
                               ) is False

    assert check_if_same_state(test_array_1,
                               test_array_1,
                               test_array_2,
                               test_array_1
                               ) is False


def test_check_if_same_state_1d():
    num_planets = 4
    num_directions = 3
    assert check_if_same_state_1d(np.zeros((num_planets, num_directions), dtype=np.int32),
                                  np.zeros((num_planets, num_directions), dtype=np.int32),
                                  np.zeros((num_planets, num_directions), dtype=np.int32),
                                  np.zeros((num_planets, num_directions), dtype=np.int32),
                                  0) is True

    test_array_1 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [-10, -11, -2]], dtype=np.int32)
    test_array_2 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [-10, -12, -2]], dtype=np.int32)

    assert check_if_same_state_1d(test_array_1,
                               test_array_1,
                               test_array_1,
                               test_array_1,
                               1
                               ) is True

    assert check_if_same_state_1d(test_array_1,
                               test_array_1,
                               test_array_2,
                               test_array_2,
                               2
                               ) is True

    assert check_if_same_state_1d(test_array_1,
                               test_array_2,
                               test_array_2,
                               test_array_1,
                               1
                               ) is False
    assert check_if_same_state_1d(test_array_1,
                               test_array_2,
                               test_array_2,
                               test_array_1,
                               2
                               ) is True
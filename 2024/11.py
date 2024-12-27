import copy
from collections import defaultdict


def get_input():
    with open("11.txt") as f:
        a = [int(i) for i in f.read().strip().split()]
    return a


def part_1(stones):
    NUM_BLINKS = 25
    for blink in range(NUM_BLINKS):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                stone_as_string = str(stones[i])
                left = int(stone_as_string[:len(stone_as_string) // 2])
                right = int(stone_as_string[len(stone_as_string) // 2:])
                stones.insert(i, left)
                stones.insert(i+1, right)
                del stones[i+2]
                i += 1
            else:
                stones[i] *= 2024

            i += 1
    return len(stones)


def part_2(stones):
    # Don't repeat calculation for the same stones
    NUM_BLINKS = 75
    stones_dict = {}
    for stone in stones:
        if stone in stones_dict:
            stones_dict[stone] += 1
        else:
            stones_dict[stone] = 1

    for blink in range(NUM_BLINKS):

        # todo: create a new dictionary each time - is this reasonable?

        previous_stones_dict = copy.deepcopy(stones_dict)
        stones_dict = defaultdict(lambda: 0)

        for stone, number in previous_stones_dict.items():

            if stone == 0:
                stones_dict[1] += number

            elif len(str(stone)) % 2 == 0:
                stone_as_string = str(stone)
                left = int(stone_as_string[:len(stone_as_string) // 2])
                right = int(stone_as_string[len(stone_as_string) // 2:])
                stones_dict[left] += number
                stones_dict[right] += number

            else:
                new_stone = stone * 2024
                stones_dict[new_stone] += number

    return sum(stones_dict.values())


if __name__ == '__main__':
    stones = get_input()
    print(part_1(copy.deepcopy(stones)))
    print(part_2(stones))

from string import ascii_letters as letters
from itertools import combinations


def get_input():
    with open("8.txt") as f:
        a = [list(row.strip()) for row in f.readlines()]
    return a


def get_coords(grid, char):
    coords = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == char:
                coords.add((row, col))
    return coords


def part_1(grid):
    possible_antennas = list(letters) + [str(i) for i in range(10)]

    antinodes = set()
    for antenna in possible_antennas:
        coords = get_coords(grid, antenna)
        if coords:
            for combination in combinations(coords, 2):
                delta = (combination[1][0] - combination[0][0], combination[1][1] - combination[0][1])
                antinode_1 = (combination[0][0] - delta[0], combination[0][1] - delta[1])
                antinode_2 = (combination[1][0] + delta[0], combination[1][1] + delta[1])
                if (antinode_1[0] >= 0) and (antinode_1[0] < len(grid)) and (antinode_1[1] >= 0) and (antinode_1[1] < len(grid)):
                    antinodes.add(antinode_1)
                if (antinode_2[0] >= 0) and (antinode_2[0] < len(grid)) and (antinode_2[1] >= 0) and (antinode_2[1] < len(grid)):
                    antinodes.add(antinode_2)

    return len(antinodes)


def part_2(grid):
    possible_antennas = list(letters) + [str(i) for i in range(10)]

    antinodes = set()
    for antenna in possible_antennas:
        coords = get_coords(grid, antenna)
        if coords:
            for combination in combinations(coords, 2):
                delta = (combination[1][0] - combination[0][0], combination[1][1] - combination[0][1])
                antinode = list(combination[0])
                while(antinode[0] >= 0) and (antinode[0] < len(grid)) and (antinode[1] >= 0) and (antinode[1] < len(grid)):
                    antinodes.add(tuple(antinode))
                    antinode[0] = antinode[0] + delta[0]
                    antinode[1] = antinode[1] + delta[1]

                antinode = list(combination[1])
                while (antinode[0] >= 0) and (antinode[0] < len(grid)) and (antinode[1] >= 0) and (antinode[1] < len(grid)):
                    antinodes.add(tuple(antinode))
                    antinode[0] = antinode[0] - delta[0]
                    antinode[1] = antinode[1] - delta[1]

    return len(antinodes)


if __name__ == '__main__':
    grid = get_input()

    print(part_1(grid))
    print(part_2(grid))

from functools import reduce


def structure_input(lines):
    games_raw = [line.split(": ")[1].split("; ") for line in lines]
    games = []
    for g in games_raw:
        rounds = []
        for r in g:
            r = r.split(", ")
            throw = {}
            for p in r:
                num, color = p.split(" ")
                throw[color] = int(num)
            rounds.append(throw)
        games.append(rounds)
    return games


if __name__ == '__main__':
    lines = [line.strip() for line in open("2_input.txt", 'r').readlines()]
    games = structure_input(lines)

    powers_total = 0
    for g in games:
        fewest_cubes = {"red": 0, "green": 0, "blue": 0}
        for r in g:
            for color, num in r.items():
                if fewest_cubes[color] < num:
                    fewest_cubes[color] = num

        power = reduce((lambda x, y: x * y), fewest_cubes.values())
        powers_total += power

    print(powers_total)

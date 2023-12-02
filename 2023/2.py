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

    # lines = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    # ]

    games = structure_input(lines)

    allowed = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    valid_ids_total = 0
    # valid_ids = []  # debug
    for i, g in enumerate(games, 1):
        valid = True
        for r in g:
            for color, num in r.items():
                if allowed[color] < num:
                    valid = False

        if valid:
            valid_ids_total += i
            # valid_ids.append(i)  # debug

    # print(valid_ids)
    print(valid_ids_total)

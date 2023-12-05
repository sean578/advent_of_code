import copy
from collections import defaultdict


def get_input(lines):

    seeds = [int(i) for i in lines[0].split("seeds: ")[1].split()]
    lines = lines[2:]

    maps = defaultdict(list)
    key = "error"

    start = True
    for line in lines:
        if start:
            key = line.split(" map:")[0]
            start = False
            continue
        if line == "":
            start = True
            continue
        maps[key].append([int(i) for i in line.split()])

    return seeds, maps


if __name__ == '__main__':
    lines = [line.strip() for line in open("5_debug.txt", 'r').readlines()]
    seeds, maps = get_input(lines)

    # input values too big to hold the full map - use ranges

    # for key, value in maps.items():
    #     print(key, value)

    map_order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"
    ]

    # todo: need to update 'seed' for next map
    final_destinations = defaultdict(list)
    for seed in seeds:
        des = copy.deepcopy(seed)  # default if no rules met
        for m in map_order:
            for rule in maps[m]:
                des_start, source_start, range_length = rule
                if des >= source_start and des <= source_start + range_length:
                    des = des - (source_start - des_start)
                    break
            final_destinations[seed].append(des)
        # seed = des

    locations = []
    for s, d in final_destinations.items():
        locations.append(d[-1])

    # print(locations)
    print(min(locations))

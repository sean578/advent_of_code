import math
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


def split(seed_pair, rule):
    seed_start, seed_range = seed_pair
    rule_dest_start, rule_source_start, rule_range = rule

    need_start_split = (seed_start <= rule_source_start <= seed_start + seed_range)
    need_stop_split = (seed_start <= rule_source_start + rule_range <= seed_start + seed_range)

    diff = rule_dest_start - rule_source_start

    seeds_updated = []
    if need_start_split and need_stop_split:
        # print("1")
        # Split seed range into 3 sections and transform (2 sections easy, 1 by rule)
        to_reduce = rule_source_start - seed_start

        seeds_updated.append((seed_start, to_reduce))  # No transform
        seeds_updated.append((rule_dest_start, rule_range))  # Transform
        seeds_updated.append((rule_source_start + rule_range, seed_range - rule_range - to_reduce))  # No transform
    elif need_start_split:
        # print("2")
        # Split seed range into 2 sections and transform (1 section easy, 1 by rule)
        to_reduce = seed_start + seed_range - (rule_source_start - rule_range)

        seeds_updated.append((seed_start, seed_range - to_reduce))  # No transform
        seeds_updated.append((seed_start + seed_range - to_reduce + diff, to_reduce))  # Transform
    elif need_stop_split:
        # print("3")
        # Split seed range into 2 sections and transform (1 section easy, 1 by rule)
        to_reduce = rule_source_start + rule_range - seed_start

        seeds_updated.append((seed_start + diff, to_reduce))  # Transform
        seeds_updated.append((seed_start + to_reduce, seed_range - to_reduce))  # No transform
    else:
        # print("4")
        # No splitting required - transform either by rule or easy
        if seed_start >= rule_source_start and seed_start + seed_range <= rule_source_start + rule_range:
            # Transform by rule
            # print("5")
            seeds_updated.append((seed_start + diff, seed_range))
        else:
            # No transformation required
            # print("6")
            seeds_updated.append(seed_pair)

    return seeds_updated


if __name__ == '__main__':
    lines = [line.strip() for line in open("5_debug.txt", 'r').readlines()]
    seeds, maps = get_input(lines)

    # input values too big to hold the full map - use ranges

    map_order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"
    ]


    seed_pairs = set()
    for i in range(0, len(seeds), 2):
        # start, stop
        seed_pairs.add((seeds[i], seeds[i] + seeds[i+1]))

    print(seed_pairs)

    # Transform each range through whole system

    # for seed_pair in seed_pairs:
    #     print(seed_pair)

    for m in [map_order[0]]:
        all_seeds = []
        print("map", m)
        print()
        for seed in seed_pairs:
            new_seed_pairs = []
            print("seed", seed)
            for rule in maps[m]:
                print("rule: dest, source, range", rule)
                new = split(seed, rule)
                print("split", new)
                print()
                new_seed_pairs.extend(new)
                # bunch of new seed ranges for the original seed range
            all_seeds.extend(new_seed_pairs)
        seed_pairs = list(set(all_seeds))

    print(min([s[0] for s in seed_pairs]))

import copy
from collections import defaultdict


def process_input(lines):

    processes_raw = []
    parts_raw = []
    process = True
    for line in lines:
        if process:
            if line == "":
                process = False
                continue
            processes_raw.append(line)
        else:
            parts_raw.append(line)

    processes = {}
    for p in processes_raw:
        name, rules_raw = p[:-1].split("{")
        rules_raw = rules_raw.split(",")
        rules = []
        for rule in rules_raw:
            rule_part, rule_val, rule_operation = None, None, None
            if "<" in rule:
                rule_part, rule_val_dest = rule.split("<")
                rule_val, rule_dest = rule_val_dest.split(":")
                rule_val = int(rule_val)
                rule_operation = "<"
            elif ">" in rule:
                rule_part, rule_val_dest = rule.split(">")
                rule_val, rule_dest = rule_val_dest.split(":")
                rule_val = int(rule_val)
                rule_operation = ">"
            else:
                # Just have a destination
                rule_dest = rule
            rules.append({
                "rule_part": rule_part,
                "rule_operation": rule_operation,
                "rule_val": rule_val,
                "rule_destination": rule_dest
            })
        processes[name] = rules

    parts = []
    for p in parts_raw:
        parts_dict = {}
        p_list = p[1:-1].split(",")
        for i in p_list:
            key, value = i.split("=")
            parts_dict[key] = int(value)
        parts.append(parts_dict)

    return processes, parts


def part_1(processes, parts):
    accepted_parts = []
    start = "in"
    for part in parts:
        rule_name = start
        accepted_rejected = False
        while not accepted_rejected:
            for rule in processes[rule_name]:
                # Go through the rules -> break & change process as required

                if rule["rule_operation"] == "<":
                    if part[rule["rule_part"]] < rule["rule_val"]:
                        rule_destination = rule["rule_destination"]
                    else:
                        # next rule
                        continue
                elif rule["rule_operation"] == ">":
                    if part[rule["rule_part"]] > rule["rule_val"]:
                        rule_destination = rule["rule_destination"]
                    else:
                        # next rule
                        continue
                elif rule["rule_operation"] is None:
                    # accept/reject or go to the process (final rule)
                    if rule["rule_destination"] == "A":
                        accepted_parts.append(part)
                        accepted_rejected = True
                        break
                    elif rule["rule_destination"] == "R":
                        accepted_rejected = True
                        break
                    else:
                        rule_name = rule["rule_destination"]
                        break
                else:
                    assert False

                # A rule is met - do what it says
                if rule_destination == "A":
                    accepted_parts.append(part)
                    accepted_rejected = True
                    # Next part
                    break
                elif rule_destination == "R":
                    accepted_rejected = True
                    # Next part
                    break
                else:
                    # Need to go to another process
                    rule_name = rule["rule_destination"]
                    break
    return accepted_parts


def get_total_part_1(accepted_parts):
    total = 0
    for a in accepted_parts:
        for v in a.values():
            total += v
    return total


def get_graph(processes):
    graph = defaultdict(list)
    for name, rules in processes.items():
        for i in range(len(rules)):
            # i is the rule we are constructing (need all rules up to that index)
            new_rules = []
            if i == 0:
                # append new rule as is
                new_rule = {key: value for key, value in rules[i].items() if
                            key != "rule_destination"}
                graph[name].append((rules[i]["rule_destination"], new_rule))
            else:
                # append the rule at the current index and the opposite of the other rules
                # Rules we don't want to be true must be opposite
                for j in range(0, i):
                    new_rule = {key: value for key, value in rules[j].items() if
                                key != "rule_destination"}
                    if new_rule["rule_operation"] == ">":
                        new_rule["rule_operation"] = "<="
                    elif new_rule["rule_operation"] == "<":
                        new_rule["rule_operation"] = ">="
                    else:
                        assert False
                    new_rules.append(new_rule)
                # Rule we want to be true is the same
                new_rule = {key: value for key, value in rules[i].items() if
                            key != "rule_destination"}
                if new_rule["rule_part"] is not None:
                    new_rules.append(new_rule)
                graph[name].append((rules[i]["rule_destination"], new_rules))
    return graph


def flatten(container):
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


if __name__ == '__main__':
    lines = [line.strip() for line in open("19_input.txt").readlines()]
    processes, _ = process_input(lines)

    path = []
    target_node_name = "A"
    graph = get_graph(processes)
    graph["R"] = []
    graph["A"] = []
    rules_for_paths = []

    def dfs(node_name, rules):

        # If we are at the target node we have found a path - print it
        if node_name == target_node_name:
            rules_for_paths.append(copy.deepcopy(rules))
        else:
            path.append(node_name)

            # If not then explore neighbours - collecting rules
            for neighbours in graph[node_name]:
                neighbour_node_name, r = neighbours
                rules.append(r)
                dfs(neighbour_node_name, rules)
                rules.pop()

            path.pop()

    # part 1
    # accepted_parts = part_1(processes, parts)
    # print(get_total_part_1(accepted_parts))

    dfs(node_name="in", rules=[])

    total_combinations = 0
    for rules_for_path in rules_for_paths:
        rules_flat = list(flatten(rules_for_path))
        # Start off with full ranges
        allowed_ranges = {
            "x": set(range(1, 4000 + 1)),
            "m": set(range(1, 4000 + 1)),
            "a": set(range(1, 4000 + 1)),
            "s": set(range(1, 4000 + 1))
        }
        # For each rule in the path, remove the range not allowed
        for rule in rules_flat:
            if rule["rule_operation"] == "<":
                not_allowed = set(range(rule["rule_val"], 4000 + 1))
                allowed_ranges[rule["rule_part"]] -= not_allowed
            elif rule["rule_operation"] == "<=":
                not_allowed = set(range(rule["rule_val"] + 1, 4000 + 1))
                allowed_ranges[rule["rule_part"]] -= not_allowed
            elif rule["rule_operation"] == ">":
                not_allowed = set(range(1, rule["rule_val"] + 1))
                allowed_ranges[rule["rule_part"]] -= not_allowed
            elif rule["rule_operation"] == ">=":
                not_allowed = set(range(1, rule["rule_val"]))
                allowed_ranges[rule["rule_part"]] -= not_allowed

        # Can assume combinations from each path are independent...
        total = 1
        for key, value in allowed_ranges.items():
            total *= len(value)
        total_combinations += total
    print(total_combinations)

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


if __name__ == '__main__':
    lines = [line.strip() for line in open("19_input.txt").readlines()]
    processes, parts = process_input(lines)

    # part 1
    accepted_parts = part_1(processes, parts)
    print(get_total_part_1(accepted_parts))

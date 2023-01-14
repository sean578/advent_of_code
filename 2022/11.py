import re

if __name__ == '__main__':
    lines = [line.strip() for line in open("11_input.txt").readlines()]

    monkeys = []
    for i in range(0, len(lines), 7):
        m = {}
        m["items"] = [int(a) for a in re.findall("\d+", lines[i+1])]
        _, m["operation"] = lines[i+2].split("Operation: ")
        m["test"] = int(re.findall("\d+", lines[i+3])[0])
        m["true"] = int(re.findall("\d+", lines[i + 4])[0])
        m["false"] = int(re.findall("\d+", lines[i + 5])[0])
        monkeys.append(m)

    num_inspections = [0]*len(monkeys)

    for r in range(1, 10000 + 1, 1):
        # print(f"Round {r}")
        for mn, m in enumerate(monkeys):
            for item in m['items']:
                num_inspections[mn] += 1
                # inspect
                old = item
                # get new worry level of item in 'new' variable
                new = -99
                exec(m['operation'])
                # new = new // 3
                new = new % 9699690
                if new % m['test'] == 0:
                    monkeys[m['true']]['items'].append(new)
                else:
                    monkeys[m['false']]['items'].append(new)
            m['items'] = []

        # for i, m in enumerate(monkeys):
        #     print(f"{i}: {m['items']}")

    print(num_inspections)
    print(sorted(num_inspections)[-1] * sorted(num_inspections)[-2])

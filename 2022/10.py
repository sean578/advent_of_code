"""
"""

if __name__ == '__main__':
    commands = [line.strip().split() for line in open("10_input.txt").readlines()]

    reg = 1
    reg_vals = [reg]
    for c in commands:
        if c[0] == "noop":
            reg_vals.append(reg)
        elif c[0] == "addx":
            reg_vals.append(reg)
            reg += int(c[1])
            reg_vals.append(reg)
        else:
            raise f"Incorrect command; {c}"

    answer = 0
    for i in range(20, len(reg_vals), 40):
        answer += i * reg_vals[i-1]

    print(answer)
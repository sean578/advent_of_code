import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


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

    print(f"Answer part 1: {answer}")

    screen_vals = []
    for i, s in enumerate(reg_vals[:-1]):
        if abs((i % 40) - s) <= 1:
            screen_vals.append(1)
        else:
            screen_vals.append(0)

    a = np.array(screen_vals).reshape((6, 40))
    plt.imshow(a)
    plt.show()

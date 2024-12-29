import numpy as np
import copy
import re
import math


def get_input():

    machines = []
    with open("13.txt") as f:
        a = []
        b = []
        prizes = []
        for line in f.readlines():
            line = line.strip()
            if line:
                if line[:10] == "Button A: ":
                    a.append([int(line[12:14]), int(line[-2:])])
                elif line[:10] == "Button B: ":
                    b.append([int(line[12:14]), int(line[-2:])])
                else:
                    prizes.append([int(i) for i in re.findall(r"\d+", line)])

    for button_a, button_b, prize in zip(a, b, prizes):
        machines.append(
            [
                [button_a[0], button_b[0], prize[0]],
                [button_a[1], button_b[1], prize[1]]
            ]
        )

    return machines


def part_1_numpy(machines):
    # todo: what if there is a float solution before an integer solution?

    TOLERANCE = 1e-5
    solutions = []
    for machine in machines:
        solution = np.linalg.solve(machine[0], machine[1])
        a = solution[0]
        b = solution[1]
        if math.isclose(a, int(a), rel_tol=TOLERANCE) and math.isclose(b, int(b), rel_tol=TOLERANCE):
            solutions.append([int(a), int(b)])

    answer = 0
    for solution in solutions:
        answer += 3 * solution[0]
        answer += solution[1]

    return answer


def part_1(machines):
    # brute force

    solutions = []
    for machine in machines:
        a, b, prize = machine
        print(a, b, prize)
        for i in range(101):
            for j in range(101):
                x_total = int(i * a[0] + j * b[0])
                y_total = int(i * a[1] + j * b[1])
                if x_total == prize[0] and y_total == prize[1]:
                    solutions.append(3 * i + j)
            else:
                continue
            break

    return sum(solutions)


def part_1_algebra(machines, TOLERANCE=1e-6):

    solution = 0
    for machine in machines:
        factor = machine[1][0] / machine[0][0]
        subtraction = [i * factor for i in machine[0]]
        machine[1] = [i - s  for i, s in zip(machine[1], subtraction)]

        division = machine[1][1]
        machine[1] = [i / division for i in machine[1]]
        button_b = machine[1][2]
        button_a = (machine[0][2] - machine[0][1] * button_b) / machine[0][0]

        if math.isclose(button_a, round(button_a), rel_tol=TOLERANCE) and math.isclose(button_b, round(button_b), rel_tol=TOLERANCE):
            solution += round(3 * button_a + button_b)

    return solution


if __name__ == '__main__':
    machines = get_input()
    machines_2 = copy.deepcopy(machines)
    print(part_1_algebra(machines))

    for machine in machines_2:
        machine[0][2] += 10000000000000
        machine[1][2] += 10000000000000

    print(part_1_algebra(machines_2, TOLERANCE=1e-14))


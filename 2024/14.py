import re
from dataclasses import dataclass
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def get_input():
    with open("14.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    robots = []
    for line in lines:
        found = re.findall(r"-?\d+", line)
        x, y, vx, vy = [int(i) for i in found]
        robots.append(Robot(x, y, vx, vy))

    return robots


def part_1(robots, grid_size, steps):

    for step in range(steps):
        for robot in robots:
            robot.x = (robot.x + robot.vx) % grid_size[0]
            robot.y = (robot.y + robot.vy) % grid_size[1]

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        if robot.x < grid_size[0] // 2:
            if robot.y < grid_size[1] // 2:
                q1 += 1
            elif robot.y >= grid_size[1] - (grid_size[1] // 2):
                q3 += 1
        elif robot.x >= grid_size[0] - (grid_size[0] // 2):
            if robot.y < grid_size[1] // 2:
                q2 += 1
            elif robot.y >= grid_size[1] - (grid_size[1] // 2):
                q4 += 1

    solution = q1 * q2 * q3 * q4

    return solution


def part_2(robots, grid_size, steps):

    for step in range(1, steps):
        for robot in robots:
            robot.x = (robot.x + robot.vx) % grid_size[0]
            robot.y = (robot.y + robot.vy) % grid_size[1]

        pos = [(robot.x, robot.y) for robot in robots]
        if len(pos) == len(set(pos)):
            print("step", step)

            plot = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
            for robot in robots:
                plot[robot.y][robot.x] = 1

            plt.imshow(plot)
            plt.show()


if __name__ == '__main__':
    robots = get_input()
    # print(part_1(robots, grid_size=(101, 103), steps=100))
    part_2(robots, grid_size=(101, 103), steps=10000)
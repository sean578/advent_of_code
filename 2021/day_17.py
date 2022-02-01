import matplotlib.pyplot as plt
import matplotlib.patches as patches
from fractions import Fraction


def probe_step(x, y, vx, vy):

    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy -= 1

    return x, y, vx, vy


def in_target(x, y, target_x, target_y):
    in_target = False
    if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
        in_target = True
    return in_target


def worth_continuing(x, y, vx, vy, target_x, target_y):
    # A trajectory has failed once either:
    #   1. x pos is greater than max x of target.
    #   2. y pos is less than min x of target
    #   3. x pos is less than min x of target & x velocity = 0

    worth = True
    if x > target_x[1] or y < target_y[0]:
        worth = False
    if x < target_x[0] and vx == 0:
        worth = False

    return worth


if __name__ == '__main__':
    TEST = False
    if TEST:
        target_x = (20, 30)
        target_y = (-10, -5)
    else:
        target_x = (156, 202)
        target_y = (-110, -69)

    STEPS_MAX = 1000
    PLOT = False

    traj_count = 0
    angles_mags = set()
    for vx_initial in range(1, target_x[1] + 1):
        for vy_initial in range(target_y[0], 10000):
            angle = Fraction(vy_initial, vx_initial)
            mag = vx_initial**2 + vy_initial**2
            angle_mag = (angle, mag)
            if angle_mag in angles_mags:
                continue
            else:
                angles_mags.add(angle_mag)
            x = 0
            y = 0
            vx = vx_initial
            vy = vy_initial
            trajectory_x = [x]
            trajectory_y = [y]

            target_found = False
            for step in range(STEPS_MAX):
                x, y, vx, vy = probe_step(x, y, vx, vy)
                target_found = in_target(x, y, target_x, target_y)
                if target_found or not worth_continuing(x, y, vx, vy, target_x, target_y):
                    break

            if target_found:
                traj_count += 1

    print('Number trajectories:', traj_count)
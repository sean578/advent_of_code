from dataclasses import dataclass


@dataclass
class Cuboid:
    x_min: int = 0
    x_max: int = 0
    y_min: int = 0
    y_max: int = 0
    z_min: int = 0
    z_max: int = 0
    sign: int = 1
    instruct: str = None


def read_data(filename):
    lines = [line.strip().split(' ') for line in open(filename).readlines()]

    cuboids = []
    for line in lines:
        c = Cuboid()

        c.instruct = line[0]
        x, y, z = line[1].split(',')
        x = x[2:]
        y = y[2:]
        z = z[2:]

        x = tuple([int(i) for i in x.split('..')])
        y = tuple([int(i) for i in y.split('..')])
        z = tuple([int(i) for i in z.split('..')])

        c.x_min, c.x_max = x
        c.y_min, c.y_max = y
        c.z_min, c.z_max = z

        cuboids.append(c)

    return cuboids


def get_intersection_cuboid(new_cuboid, current_cuboid):
    # Return a cuboid of overlap region

    # Return None if cuboids don't overlap...
    if new_cuboid.x_max < current_cuboid.x_min or new_cuboid.y_max < current_cuboid.y_min or new_cuboid.z_max < current_cuboid.z_min:
        return None
    if current_cuboid.x_max < new_cuboid.x_min or current_cuboid.y_max < new_cuboid.y_min or current_cuboid.z_max < new_cuboid.z_min:
        return None

    c = Cuboid()
    c.instruct = 'Intersection'
    c.sign = -current_cuboid.sign
     
    c.x_min = max(new_cuboid.x_min, current_cuboid.x_min)
    c.x_max = min(new_cuboid.x_max, current_cuboid.x_max)
    
    c.y_min = max(new_cuboid.y_min, current_cuboid.y_min)
    c.y_max = min(new_cuboid.y_max, current_cuboid.y_max)
    
    c.z_min = max(new_cuboid.z_min, current_cuboid.z_min)
    c.z_max = min(new_cuboid.z_max, current_cuboid.z_max)

    return c


def get_cube_size(c):
    size = (c.x_max + 1 - c.x_min) * (c.y_max + 1 - c.y_min) * (c.z_max + 1 - c.z_min)
    size *= c.sign
    return size


if __name__ == '__main__':
    cuboids = read_data('day_22.txt')

    the_cuboids = [cuboids[0]]  # Assumes first cuboid is 'on'

    # Iterate through each new cuboid
    i = 0
    for new_cuboid in cuboids[1:]:
        print(f'Status: {100 * i / len(cuboids):.1f} %')
        i += 1

        # tc = copy.deepcopy(the_cuboids)
        new_intersections = []

        # Check against all current cuboids
        for current_cuboid in the_cuboids:
            intersection = get_intersection_cuboid(new_cuboid, current_cuboid)
            if intersection:
                new_intersections.append(intersection)

        # Finally add the cuboid if on
        if new_cuboid.instruct == 'on':
            new_intersections.append(new_cuboid)

        the_cuboids += new_intersections

    # Sum up the cube sizes
    the_sum = 0
    for c in the_cuboids:
        the_sum += get_cube_size(c)
    print('Total sum:', the_sum)

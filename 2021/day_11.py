import numpy as np


def read_data(filename):
    data_list = [[int(i) for i in list(line.strip())] for line in open(filename).readlines()]
    return np.array(data_list)


def increase_energy(data):
    data += 1
    return data


def get_flash_coords(data, flash_mask):
    flash_coords = []
    above9 = np.argwhere(data > 9)
    for coord in above9:
        if flash_mask[coord[0], coord[1]] == 0:
            flash_coords.append(coord)
            flash_mask[coord[0], coord[1]] = 1
    return flash_coords, flash_mask


def get_neighbours(coord, size_x, size_y):
    adjacent_coords = []
    for delta_x in (-1, 0, 1):
        for delta_y in (-1, 0, 1):
            if delta_x != 0 or delta_y != 0:
                x_new = coord[0] + delta_x
                y_new = coord[1] + delta_y
                if 0 <= x_new < size_x and 0 <= y_new < size_y:
                    adjacent_coords.append([x_new, y_new])
    return adjacent_coords


if __name__ == '__main__':
    data = read_data('day_11.txt')
    size_x, size_y = data.shape

    num_flashes = 0
    for i in range(100):

        # 1. Increase energy of all elements
        data = increase_energy(data)

        # 2. Get coords of all elements that will flash
        flash_mask = np.zeros((size_x, size_y))
        while True:
            new_flashes, flash_mask = get_flash_coords(data, flash_mask)
            if len(new_flashes) == 0:
                break

            # 3. Increase energy of adjacent elements to flashes
            for flash in new_flashes:
                energy_from_flash = get_neighbours(flash, size_x, size_y)
                for recipient in energy_from_flash:
                    data[recipient[0], recipient[1]] += 1
            # 4. Check again if any new elements have flashed (back to stop 2)

        # 5. Done with this time step - Set all elements that have flashed to 0
        data[flash_mask == 1] = 0
        num_flashes += np.count_nonzero(flash_mask)

        print('After iteration', i+1)
        print(data)

    print('Number of flashes', num_flashes)


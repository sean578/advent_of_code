import numpy as np
import sys
np.set_printoptions(threshold=np.inf)
import copy


def read_data(filename):
    lines = [line.strip() for line in open(filename).readlines()]

    image_enhancement = np.array([1 if i == '#' else 0 for i in lines[0]], np.uint8)
    image = np.vstack([np.array([1 if i == '#' else 0 for i in l], np.uint8) for l in lines[2:]])

    return image_enhancement, image


def get_neighbours(image, image_shape, deltas, loc):
    # Todo: Plenty to optimise here

    neighbour_values = []
    for d in deltas:
        if 0 <= loc[0] + d[0] < image_shape[0] and 0 <= loc[1] + d[1] < image_shape[1]:
            neighbour_values.append(str(image[loc[0] + d[0], loc[1] + d[1]]))
        else:
            pass
            # print('Out of range')
            neighbour_values.append('0')

    return neighbour_values


if __name__ == '__main__':
    image_enhancement, image = read_data('day_20.txt')
    num_enhancements = 50

    image = np.pad(image, pad_width=num_enhancements + 3, mode='constant', constant_values=0)

    print('Image enhancement size:', image_enhancement.shape)
    image_shape = image.shape
    print('Image size:', image.shape)

    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]  # y, x

    for i in range(num_enhancements):
        print('Enhancement:', i+1)
        image_enhanced = np.zeros_like(image)
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                nv = get_neighbours(image, image_shape, deltas, (y, x))
                binary_string = ''.join(nv)
                index = int(binary_string, 2)
                image_enhanced[y, x] = image_enhancement[index]
        image_enhanced[0,:] = image_enhanced[1, 1]
        image_enhanced[-1, :] = image_enhanced[1, 1]
        image_enhanced[:, 0] = image_enhanced[1, 1]
        image_enhanced[:, -1] = image_enhanced[1, 1]
        image = copy.deepcopy(image_enhanced)

    num_pixels_lit = np.count_nonzero(image)
    print('Number of pixels lit:', num_pixels_lit)


import numpy as np

input_data = open('input.txt')
input_config = []
for line in input_data:
    input_config.append(line)

# input_config = [
#     '.#.#.#',
#     '...##.',
#     '#....#',
#     '..#...',
#     '#.#..#',
#     '####..',
# ]

input_as_array = np.zeros((100, 100))
# input_as_array = np.zeros((6, 6))

# create an array with each light as an element
i = 0
for row in input_config:
    j = 0
    for light in row:
        if light == '#':
            input_as_array[i, j] = 1
        elif light == '.':
            input_as_array[i, j] = 0
        j = j+1
    i = i+1

for i in range(100):

    # create a new array
    new_array = np.ones(input_as_array.shape)*9

    # loop through each element of initial array
    size_y, size_x = input_as_array.shape
    for y in range(size_y):
        for x in range(size_x):

            # get the neighbours subset
            nn_values = []
            if y > 0 and x > 0:
                nn_values.append(input_as_array[y-1, x-1])
            if x > 0:
                nn_values.append(input_as_array[y, x-1])
            if x > 0 and y < size_y-1:
                nn_values.append(input_as_array[y+1, x-1])
            if y < size_y-1:
                nn_values.append(input_as_array[y+1, x])
            if y > 0:
                nn_values.append(input_as_array[y-1, x])
            if y < size_y-1 and x < size_y-1:
                nn_values.append(input_as_array[y+1, x+1])
            if x < size_x-1:
                nn_values.append(input_as_array[y, x+1])
            if y > 0 and x < size_x-1:
                nn_values.append(input_as_array[y-1, x+1])

            num_ones = nn_values.count(1)
            if input_as_array[y, x] == 1:
                if num_ones == 2 or num_ones == 3:
                    new_array[y, x] = 1
                else:
                    new_array[y, x] = 0
            elif input_as_array[y, x] == 0:
                if num_ones == 3:
                    new_array[y, x] = 1
                else:
                    new_array[y, x] = 0
    input_as_array = new_array
    input_as_array[0, 0] = 1.0
    input_as_array[0, 99] = 1.0
    input_as_array[99, 0] = 1.0
    input_as_array[99, 99] = 1.0
# print(new_array)
print(np.count_nonzero(new_array == 1))
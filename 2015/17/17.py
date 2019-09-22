# import numpy as np

# container_sizes = [1,2,3,4,5,6,7,8,9]
# eggnog_total = 10

container_sizes = [
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42
]

eggnog_total = 150

# print(container_sizes[0])
# print(np.array([] + [container_sizes[0]]))


def recursive_combinations(sizes, target, comb, count, min_size):
    if sum(comb) == target:
        if len(comb) <= min_size:
            min_size = len(comb)
            print('a combination is:', comb, sum(comb))
            count = count + 1
        return count, min_size  # Found a combination
    if sum(comb) > target:
        return count, min_size  # No way to sum to target

    # Now we create a new combination to try
    for i in range(len(sizes)):
        partial = comb + [sizes[i]]
        rest_of_array = sizes[i+1:]
        # print(partial)
        # print(rest_of_array)
        count, min_size = recursive_combinations(rest_of_array, target, partial, count, min_size)

    return count, min_size


if __name__ == "__main__":
    count, min_size = recursive_combinations(container_sizes, eggnog_total, [], 0, 999)
    count, min_size = recursive_combinations(container_sizes, eggnog_total, [], 0, min_size)
    print(count, min_size)

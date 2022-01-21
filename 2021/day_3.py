import copy


def get_most_least_common(nums, index, most_common=True):

    sum = 0
    for n in nums:
        if n[index] == '0':
            sum -= 1
        else:
            sum += 1

    if sum >= 0:
        if most_common:
            mc = '1'
        else:
            mc = '0'
    else:
        if most_common:
            mc = '0'
        else:
            mc = '1'

    return mc


def find_rating(nums, num_digits, most_common=True):

    for i in range(num_digits):
        # Get most common in each col of words left
        mc = get_most_least_common(nums=nums, index=i, most_common=most_common)

        # Filter the nums
        if len(nums) == 1:
           break
        else:
            nums = list(filter(lambda x: x[i] == mc, nums))

    return nums[0]


if __name__ == '__main__':

    # Hold numbers as strings
    nums = [i.strip() for i in open('day_3.txt').readlines()]
    num_digits = len(nums[0])

    nums_o2 = copy.deepcopy(nums)
    nums_co2 = copy.deepcopy(nums)

    nums_o2 = find_rating(nums_o2, num_digits, most_common=True)
    nums_co2 = find_rating(nums_co2, num_digits, most_common=False)

    print(int(nums_o2, 2) * int(nums_co2, 2))
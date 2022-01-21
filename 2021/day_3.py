import copy


def get_most_least_common(nums, index, most_common=True):

    sum = 0
    for n in nums:
        if n[index] == '0':
            sum -= 1
        else:
            sum += 1
    if sum > 0:
        if most_common:
            mc = '1'
        else:
            mc = '0'
    elif sum < 0:
        if most_common:
            mc = '0'
        else:
            mc = '1'
    else:
        if most_common:
            mc = '1'
        else:
            mc = '0'

    return mc


if __name__ == '__main__':

    # Hold numbers as strings
    nums = [i.strip() for i in open('day_3.txt').readlines()]
    num_digits = len(nums[0])

    nums_o2 = copy.deepcopy(nums)
    nums_co2 = copy.deepcopy(nums)


    for i in range(num_digits):

        print('len', len(nums_o2))
        print(nums_o2)

        # Get most common in each col of words left
        mc = get_most_least_common(nums=nums_o2, index=i, most_common=True)

        # Filter the nums
        ok_o2 = []
        if len(nums_o2) == 1:
            print('found o2')
            break
        else:
            for l in nums_o2:
                if l[i] == mc:
                    ok_o2.append(l)
            nums_o2 = copy.deepcopy(ok_o2)


    for i in range(num_digits):

        # Get least common in each col of words left
        lc = get_most_least_common(nums=nums_co2, index=i, most_common=False)

        # Filter the nums
        ok_co2 = []

        if len(nums_co2) == 1:
            print('found co2')
            break
        else:
            for l in nums_co2:
                if l[i] == lc:
                    ok_co2.append(l)
            nums_co2 = copy.deepcopy(ok_co2)



    print(nums_o2)
    print(nums_co2)
    print(int(nums_o2[0], 2) * int(nums_co2[0], 2))
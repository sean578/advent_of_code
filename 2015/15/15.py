import numpy as np


def find_sum_combs_to_target(target):
    """ Find sums of 4 numbers that add to target.
    """
    
    combinations = []
    for x_1 in range(0, target+1):
        for x_2 in range(0, target+1-x_1):
            for x_3 in range(0, target+1-x_1-x_2):
                for x_4 in range(0, target+1-x_1-x_2-x_3):
                    x_4 = target - x_1 - x_2 - x_3
                    combinations.append((x_1, x_2, x_3, x_4))
    
    return combinations


def put_ingredient_properties_in_array(input_data):

    calories_array = []
    params_arrays = []
    for line in input_data.readlines():
        # the_names = line.split(':')[0]
        the_params = line.split(':')[1].strip('\n').split(',')
        
        param_array = []
        for param in the_params:
            param_array.append(int(param.split(' ')[2]))

        calories_array.append(param_array[-1])
            
        del param_array[-1]
        params_arrays.append(param_array)
        
    return np.array(params_arrays), np.array(calories_array)
    

######################################################
# Get input data & put into an array
######################################################

input_data = open('input.txt', 'r')

data, calories = put_ingredient_properties_in_array(input_data)
print('Input data\n', data)
print('Calories\n', calories)

######################################################
# Get combinations that sum up to 100 teaspoons
######################################################

combinations = find_sum_combs_to_target(100)

best_combination = None
max_score = 0
flag = True
for combination in combinations:
    
    teaspoons = np.array(combination)
    if flag:
        print('combination\n', combination)
        print('teaspoons\n', teaspoons)

    # Sum all the teaspoons for each ingredient
    all_teaspoons = np.multiply(data.T, teaspoons).T
    if flag:
        print('all_teaspoons\n', all_teaspoons)
    
    
    # multiply each parameter
    param_sums = all_teaspoons.sum(0)
    if flag:
        print('param_sums\n', param_sums)
    
    # If a parameter total is < 0 then set to 0
    param_sums_clipped = param_sums.clip(min=0)
    if flag:
        print('param_sums_clipped\n', param_sums_clipped)
    
    # sum up the final params
    total = param_sums_clipped.prod()
    if flag:
        print('total\n', total)
    
    if total > max_score:
        if np.sum(np.multiply(calories.T, teaspoons).T) == 500:
            max_score = total
            best_combination = combination
        
    flag = False
        
print('max_score', max_score)
print('best_combination', combination)





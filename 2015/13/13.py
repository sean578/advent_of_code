import itertools as it

the_file = open('input.txt', 'r')

def get_line_data(line):
    
    line_array = line.strip('\n').split(' ') # remove the newline character
    name_a = line_array[0]
    name_b = line_array[10][:-1] # remove the full stop
    gain_lose = line_array[2]
    happiness = int(line_array[3])
    if gain_lose == 'lose':
        happiness = -1*happiness
        
    return [name_a, name_b , happiness]

#### Put the usful input data into an array ####

input_data = []
for line in the_file.readlines():
    input_data.append(get_line_data(line))
    
#### Get a list of the names ####
    
names = []
for line in input_data:
    if line[0] not in names:
        names.append(line[0])

names.append('Sean')
print('The names = ', names)

#### Create a dictionary for each name with a list for each other name ####

the_dict = {}
for name in names:
    the_dict[name] = [0 for name in names]
    
#### Fill up the dictionaries with the happiness scores ####
    
for line in input_data:
    the_dict[line[0]][names.index(line[1])] = line[2]

print(the_dict['Alice'])

#### Go through each permutation ###

perms = it.permutations(names)
highest_cost = -9999999999
for perm in perms:
    cost = 0
    i = 0
    for i in range(len(perm)):
        if i == len(perm) - 1:
            cost = cost + the_dict[perm[i]][names.index(perm[0])]
        else:
            cost = cost + the_dict[perm[i]][names.index(perm[i+1])]
        cost = cost + the_dict[perm[i]][names.index(perm[i-1])]
        
    if cost > highest_cost:
        highest_cost = cost

print(highest_cost)
        
        
        
        
        
    

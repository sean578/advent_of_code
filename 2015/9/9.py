import itertools

data = open('input.txt', 'r')

line_array = []
for line in data:
    
    line = line.strip().replace(' = ', ' to ')
    line_array.append(line.split(' to '))
    
print(line_array[0])

location_list = []

for line in line_array:
    for i in range(2):
        if line[i] not in location_list:
            location_list.append(line[i])
            
print(location_list)

location_orders = list(itertools.permutations(location_list))

print(location_orders[0])

distance_min = 999
distance_max = 0
for order in location_orders:
    distance = 0
    for i in range(len(order) - 1):
        #search for distance for order[i], order[i+1]
        for data in line_array:
            if order[i] == data[0] or order[i] == data[1]:
                if order[i+1] == data[0] or order[i+1] == data[1]:
                    distance = distance + int(data[2])
    if distance < distance_min:
        distance_min = distance
    if distance > distance_max:
        distance_max = distance
        
print('min distance', distance_min)
print('max distance', distance_max)
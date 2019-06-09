input_data = open('input.txt', 'r')

time = 2503

def get_data(line):
    the_data = {}
    line_as_list = line.strip('\n').strip('.').split(' ')
    the_data['speed'] = int(line_as_list[3])
    the_data['go_time'] = int(line_as_list[6])
    the_data['stop_time'] = int(line_as_list[13])
    return the_data

def calc_distance(the_data, time):
    num_start_and_stop = time // (the_data['go_time'] + the_data['stop_time'])
    time_left_over = time % (the_data['go_time'] + the_data['stop_time'])
    time_go = num_start_and_stop*the_data['go_time']
    if time_left_over >= the_data['go_time']:
        time_go = time_go + the_data['go_time']
    else:
        time_go = time_go + time_left_over
    return time_go * the_data['speed']

distance_max = 0
for line in input_data.readlines():
    the_data = get_data(line)
    distance = calc_distance(the_data, time)
    if distance > distance_max:
        distance_max = distance
        
print(distance_max)
    
# 1320 too low
# 2610 too low
    
    
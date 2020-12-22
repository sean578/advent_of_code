def load_input(filename):
    raw = []
    for line in open(filename).readlines():
        raw.append(line.strip('\n'))

    start = int(raw[0])
    busses = set(raw[1].split(','))
    busses.remove('x')

    return start, [int(i) for i in busses]


if __name__ == '__main__':
    filename = 'day_13.txt'
    start, busses = load_input(filename)

    print(start)
    print(busses)

    w = [start % bus for bus in busses]

    wait_times = []
    for time, bus in zip(w, busses):
        if time == 0:
            wait_times.append(0)
        else:
            wait_times.append(-time + bus)

    min_wait_time = min(wait_times)

    quickest_bus_index = wait_times.index(min_wait_time)

    quickest_bus = busses[quickest_bus_index]

    print('wait times', wait_times)
    print('min wait time', min_wait_time)
    print('quicket bus index', quickest_bus_index)
    print('quickest bus', quickest_bus)

    print('Answer part 1:', quickest_bus * min_wait_time)
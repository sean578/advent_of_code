def get_input():
    with open("9.txt") as f:
        a = f.read().strip()
    return a


def get_structure(disk_map):
    disk_map_structure = []
    value = 0
    for i, size in enumerate(disk_map):
        if i % 2 == 0:
            disk_map_structure.append(["block", int(size), value])
            value += 1
        else:
            disk_map_structure.append(["space", int(size), None])
    return disk_map_structure


def checksum(disk_map_structure):
    checksum = 0
    m = -1
    for block in disk_map_structure:
        if block[0] == "block" and block[1] > 0:
            n = block[1] + m
            this_checksum = 0.5 * block[2] * (n * (n + 1) - m * (m + 1))
            checksum += this_checksum
            m += block[1]
        elif block[1] > 0:
            m += block[1]

    return int(checksum)


def part_1(disk_map):
    disk_map_structure = get_structure(disk_map)

    write_pointer = 0
    read_pointer = len(disk_map) - 1
    while write_pointer < read_pointer:
        # Move write pointer to the next space if not already there
        if disk_map_structure[write_pointer][0] != "space":
            write_pointer += 1
            continue
        if disk_map_structure[write_pointer][1] == 0:
            write_pointer += 1
            continue
        # Move read pointer to the next block if not already there
        if disk_map_structure[read_pointer][0] != "block":
            read_pointer -= 1
            continue
        if disk_map_structure[read_pointer][1] == 0:
            read_pointer -= 1
            continue

        # Move as many into the space as possible from the current read position

        assert disk_map_structure[read_pointer][0] == "block"
        max_to_read = disk_map_structure[read_pointer][1]
        value_to_read = disk_map_structure[read_pointer][2]

        assert disk_map_structure[write_pointer][0] == "space"
        max_to_write = disk_map_structure[write_pointer][1]

        if max_to_write >= max_to_read:
            amount_to_move = max_to_read
        else:
            amount_to_move = max_to_write

        # move the whole block
        disk_map_structure.insert(write_pointer, ["block", amount_to_move, value_to_read])
        # due to above insertion, need to update pointers to be able to stay in same play
        read_pointer += 1
        write_pointer += 1
        disk_map_structure[read_pointer][1] -= amount_to_move
        disk_map_structure[write_pointer][1] -= amount_to_move

    return checksum(disk_map_structure)


def part_2(disk_map):
    disk_map_structure = get_structure(disk_map)

    read_pointer = len(disk_map) - 1
    while read_pointer > 0:
        if disk_map_structure[read_pointer][0] != "block":
            read_pointer -= 1
            continue

        required_size = disk_map_structure[read_pointer][1]
        file_value = disk_map_structure[read_pointer][2]

        for i in range(read_pointer):
            if disk_map_structure[i][0] != "space":
                continue
            if disk_map_structure[i][1] < required_size:
                continue

            disk_map_structure.insert(i, ["block", required_size, file_value])
            disk_map_structure[i+1][1] -= required_size
            read_pointer += 1

            # create the space from moving the file
            disk_map_structure[read_pointer][0] = "space"
            disk_map_structure[read_pointer][2] = None

            break

        read_pointer -= 1

    return checksum(disk_map_structure)


if __name__ == '__main__':
    disk_map = get_input()
    print(part_1(disk_map))
    print(part_2(disk_map))

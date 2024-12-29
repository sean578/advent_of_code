def get_input():
    with open("12.txt") as f:
        grid = [list(row.strip()) for row in f.readlines()]
    return grid


def get_neighbours(grid, location):
    num_rows = len(grid)
    num_cols = len(grid[0])

    neighbours = []
    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        proposed = (location[0] + delta[0], location[1] + delta[1])
        if (proposed[0] < num_rows) and (proposed[1] < num_cols) and (proposed[0] >= 0) and (proposed[1] >= 0):
            neighbours.append(proposed)

    return neighbours


def get_regions(grid):
    regions = []
    values = []

    # todo: use a binary array instead?
    already_used = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in already_used:
                continue

            # Do a flood fill from this location
            to_search = [(row, col)]
            value = grid[row][col]
            this_region = set()
            while to_search:
                current_location = to_search.pop()
                already_used.add(current_location)
                this_region.add(current_location)

                # check neighbours - if same value, add to check
                neighbours = get_neighbours(grid, current_location)
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] == value:
                        if neighbour not in this_region:
                            to_search.append(neighbour)

            regions.append(this_region)
            values.append(value)

    return regions, values


def get_areas(regions):
    return [len(region) for region in regions]


def get_perimeters(grid, regions, values):
    perimeters = []

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for value, region in zip(values, regions):
        num_edges = 0
        for coord in region:
            for delta in deltas:
                location_check = (coord[0] + delta[0], coord[1] + delta[1])
                # if we are outside the grid then it is an edge
                if location_check[0] < 0 or location_check[1] < 0 or location_check[0] >= len(grid) or location_check[1] >= len(grid[0]):
                    num_edges += 1
                    continue
                if grid[location_check[0]][location_check[1]] != value:
                    num_edges += 1
        perimeters.append(num_edges)
    return perimeters


def part_1(grid):

    regions, values = get_regions(grid)
    areas = get_areas(regions)
    perimeters = get_perimeters(grid, regions, values)

    # get the final answer
    answer = 0
    for area, perimeter in zip(areas, perimeters):
        answer += area * perimeter

    return answer


def get_diffs(regions):
    diffs = []

    for region in regions:
        region_diffs = []
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            region_direction_diff = set()
            for coord in region:
                if (coord[0] + direction[0], coord[1] + direction[1]) not in region:
                    region_direction_diff.add(coord)
            region_diffs.append(region_direction_diff)
        diffs.append(region_diffs)
    return diffs


def count_edges(diffs):

    # similar to finding the regions but now do it on a set rather than a grid
    num_edges = []

    for region_diffs in diffs:
        num_edges_region = 0
        for diff_direction in region_diffs:
            regions = []
            done = set()

            for coord in diff_direction:

                if coord in done:
                    continue

                # flood fill to create a region from this point

                # initialise the points to search
                to_search = {coord}

                # while we still have connected points to search
                region = set()
                while to_search:
                    current = to_search.pop()
                    region.add(current)
                    done.add(current)

                    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        candidate = (current[0] + direction[0], current[1] + direction[1])
                        if (candidate in diff_direction) and (candidate not in done):
                            to_search.add(candidate)

                regions.append(region)
            num_edges_region += len(regions)
        num_edges.append(num_edges_region)

    return num_edges


def part_2(grid):

    regions, values = get_regions(grid)
    diffs = get_diffs(regions)
    areas = get_areas(regions)
    num_edges = count_edges(diffs)

    # get the final answer
    answer = 0
    for area, edges in zip(areas, num_edges):
        answer += area * edges

    return answer


if __name__ == '__main__':
    grid = get_input()
    print(part_1(grid))
    print(part_2(grid))

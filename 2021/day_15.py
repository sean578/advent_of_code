import heapq
import math
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000,
    formatter=dict(float=lambda x: "%.3g" % x))


def read_data(filename):
    return np.array([[int(i) for i in list(line.strip())] for line in open(filename)], np.int8)


def create_larger_map(matrix):
    matrix_1 = matrix
    matrix_2 = matrix + 1
    matrix_3 = matrix + 2
    matrix_4 = matrix + 3
    matrix_5 = matrix + 4
    matrix_top = np.concatenate((matrix_1, matrix_2, matrix_3, matrix_4, matrix_5), axis=1)

    matrix_1 = matrix_top
    matrix_2 = matrix_top + 1
    matrix_3 = matrix_top + 2
    matrix_4 = matrix_top + 3
    matrix_5 = matrix_top + 4

    matrix_large = np.concatenate((matrix_1, matrix_2, matrix_3, matrix_4, matrix_5), axis=0)
    a = np.where(matrix_large > 9, matrix_large - 9, matrix_large)
    return a


def get_neighbours(matrix, node, moves):
    # Nodes, moves all (row, column)

    neighbours = []
    for move in moves:
        n = (node[0] + move[0], node[1] + move[1])
        if 0 <= n[0] < len(matrix) and 0 <= n[1] < len(matrix[0]):
            neighbours.append(n)

    return neighbours


def initialise(matrix, start_node):
    # Priority queue, results, visited

    # DATA STRUCTURES
    # Priority queue to quickly get min distance mode (min heap)
    queue = [(0, start_node)]  # 0 distance to start node
    heapq.heapify(queue)  # Not required

    # Visited (set)
    r, c = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]

    # Results dict (parent & distance)
    distances = [[math.inf for _ in range(c)] for _ in range(r)]
    distances[start_node[0]][start_node[1]] = 0
    parents = [[None for _ in range(c)] for _ in range(r)]

    return queue, visited, distances, parents


def dijkstra(matrix, moves, queue, visited, distances, parents):

    while queue:
        # Pop min element, add to visited, results
        # Keep popping till find element not visited
        found = False
        dist, n = None, None
        while not found:
            dist, n = heapq.heappop(queue)
            if not visited[n[0]][n[1]]:
                found = True

        # For neighbours
        for neighbour in get_neighbours(matrix, n, moves):
            # If new distance less than results distance then update results & push to queue
            new_dist = dist + matrix[neighbour[0]][neighbour[1]]
            old_dist = distances[neighbour[0]][neighbour[1]]
            if new_dist < old_dist:
                heapq.heappush(queue, (new_dist, neighbour))
                parents[neighbour[0]][neighbour[1]] = n
                distances[neighbour[0]][neighbour[1]] = new_dist

    return distances, parents


def get_shortest_path(parents, end_node):
    path = []
    n = end_node
    while n:
        path.append(n)
        n = parents[n[0]][n[1]]

    path.reverse()
    return path


if __name__ == '__main__':
    """
    Task is to get from top left corner to bottom right corner of a grid in shortest path.
    Can only move right, down or on diagonal between these 2.
    Grid elements give the cost of the move.

    Solution:
    - Dijkstra if weights are positive
    """

    # PROBLEM DEFINITION

    # Have a grid of numbers - gives the cost of travelling through that node
    # Start in top left, finish in bottom right
    # Allow moving right, down & diagonal in between
    matrix = read_data('day_15.txt')
    matrix = create_larger_map(matrix)
    start_node = (0, 0)
    end_node = (matrix.shape[1]-1, matrix.shape[0]-1)
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # SOLUTION
    queue, visited, distances, parents = initialise(matrix, start_node)
    distances, parents = dijkstra(matrix, moves, queue, visited, distances, parents)
    shortest_path = get_shortest_path(parents, end_node)

    # PRINT RESULTS

    print('shortest path', shortest_path)
    print('Answer:', distances[-1][-1])
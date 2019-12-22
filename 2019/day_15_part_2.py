import numpy as np
import matplotlib.pyplot as plt


def plot_array(maze):

    plt.imshow(maze, cmap='gray', interpolation='none', origin='lower')
    plt.xticks([x - 0.5 for x in list(range(0, 50))])
    plt.yticks([y - 0.5 for y in list(range(0, 50))])
    plt.grid(linewidth=0.1)
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    frame1.axes.yaxis.set_ticklabels([])
    # plt.savefig('maze.png')
    plt.show()


# Read in full array from part 1
full_maze = np.load('full_maze.npy')
full_maze[9, 27] = 1  # remove the location mark
full_maze[7, 43] = 5  # define where the o2 is
print('The indicies used:', set(full_maze.flatten()))

# Make a copy of the array:
maze_copy = full_maze.copy()

for _ in range(326):
    # Iterate through original array, creating a new array (initially copying original maze array):
    for y in range(full_maze.shape[0]):
        for x in range(full_maze.shape[1]):
            # if element = oxygen set surrounding elements equal to oxygen if not wall
            if full_maze[y, x] == 5:
                if full_maze[y+1, x] == 2:
                    maze_copy[y+1, x] = 5
                if full_maze[y-1, x] == 2:
                    maze_copy[y-1, x] = 5
                if full_maze[y, x+1] == 2:
                    maze_copy[y, x+1] = 5
                if full_maze[y, x-1] == 2:
                    maze_copy[y, x-1] = 5

    full_maze = maze_copy.copy()
plot_array((full_maze))

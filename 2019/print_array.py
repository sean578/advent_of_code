import numpy as np
import matplotlib.pyplot as plt

maze = np.load('maze.npy')
print(maze)

plt.imshow(maze, cmap='gray', interpolation='none')
plt.xticks([x-0.5 for x in list(range(0, 50))])
plt.yticks([y-0.5 for y in list(range(0, 50))])
plt.grid(linewidth=0.1)
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
plt.savefig('maze.png')
plt.show()

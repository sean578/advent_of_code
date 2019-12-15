from intcode_day_13 import IntCode
import numpy as np
import matplotlib.pyplot as plt

try:
    intcode = IntCode('day_13.txt')  # Initialise the program
except:
    raise Exception('Cannot read program file')

# Get all of the output values from the program into a list
done = False
while not done:
    intcode.command()
    if 99 in intcode.output_values:
        done = True
print(intcode.output_values)

# Split the output_values up into instructions
instructions = []
i = 0
while i < len(intcode.output_values):
    instructions.append(intcode.output_values[i:i+3])
    i = i + 3
instructions.pop(-1)  # Remove the halt output
print(instructions)

# Set up a grid to hold the instructions
instructions_numpy = np.array(instructions, dtype=np.int32)
max_x, max_y = instructions_numpy[:, 0].max(), instructions_numpy[:, 1].max()
print('screen_dimensions', max_x, max_y)
the_screen = np.zeros((max_y+1, max_x+1), dtype=np.int32)

# Create the screen
for instruction in instructions:
    the_screen[instruction[1], instruction[0]] = instruction[2]

# Count elements
element, counts = np.unique(the_screen, return_counts=True)
the_elements = dict(zip(element, counts))
print(the_elements)

# Plot the screen
plt.imshow(the_screen == 2, cmap='gray')
plt.show()




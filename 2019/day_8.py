import numpy as np

layer_shape = (6, 25)  # 6 tall, 25 wide
layer_size = layer_shape[0]*layer_shape[1]
print('layer size', layer_size)

image_data = open('day_8.txt').read().strip()
print('length image data', len(image_data))

num_layers = len(image_data) // layer_size
print('num layers', num_layers)

layers = []
for layer in range(num_layers):
    layers.append(image_data[layer*layer_size:(layer+1)*layer_size])

num_zeros = []
for layer in layers:
    num_zeros.append(layer.count('0'))

layer_with_least_zeros = np.argmin(np.array(num_zeros))
print('Layer with least zeros', layer_with_least_zeros)

num_ones = layers[layer_with_least_zeros].count('1')
num_twos = layers[layer_with_least_zeros].count('2')
print('answer', num_ones * num_twos)


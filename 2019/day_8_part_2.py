import numpy as np
import matplotlib.pyplot as plt

layer_shape = (6, 25)  # 6 tall, 25 wide
layer_size = layer_shape[0]*layer_shape[1]
print('layer size', layer_size)

image_data = open('day_8.txt').read().strip()
print('length image data', len(image_data))

num_layers = len(image_data) // layer_size
print('num layers', num_layers)

layers = []
for layer in range(num_layers):
    layer_as_string = image_data[layer * layer_size:(layer + 1) * layer_size]
    layers.append([int(i) for i in layer_as_string])

layers = np.array(layers, dtype=np.int8).reshape(num_layers, *layer_shape)
print(layers.shape)

uncoded_image = np.ones(layer_shape)

for layer in layers:
    np.copyto(uncoded_image, layer, where=(layer == 0))

# for y in range(layers.shape[1]):
#     for x in range(layers.shape[2]):
#         z = 0
#         while True:
#             pixel = layers[z, y, x]
#             if pixel == 2:
#                 z += 1
#             else:
#                 uncoded_image[y, x] = pixel
#                 break

plt.imshow(uncoded_image, cmap='gray')
plt.show()

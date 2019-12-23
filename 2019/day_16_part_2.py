import numpy as np

# Get the input signal
input_signal = open('day_16.txt').read().strip() * 10000
offset = int(input_signal[0:7])
print('offset', offset)
input_signal_list = np.array([int(i) for i in input_signal])
print('initial')
print(input_signal_list, '\n')

# loop over the phases
sig = input_signal_list
for phase in range(100):
    print('phase, sig', phase, sig)
    sig = np.cumsum(sig[::-1])[::-1]
    sig = np.mod(sig, 10)

print(sig[offset:offset+8])


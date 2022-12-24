"""
"""

if __name__ == '__main__':
    signal = open("6_input.txt").readline().strip()

    buffer = []
    for i, s in enumerate(signal):
        if i <= 3:
            buffer.append(s)
        else:
            assert len(buffer) == 4, buffer
            if len(set(buffer)) == len(buffer):
                print("Found", i)
                break
            else:
                buffer.pop(0)
                buffer.append(s)


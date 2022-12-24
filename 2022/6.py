"""
"""

if __name__ == '__main__':
    signal = open("6_input.txt").readline().strip()

    LEN = 14

    buffer = []
    for i, s in enumerate(signal):
        if i <= LEN - 1:
            buffer.append(s)
        else:
            assert len(buffer) == LEN, buffer
            if len(set(buffer)) == len(buffer):
                print("Found", i)
                break
            else:
                buffer.pop(0)
                buffer.append(s)


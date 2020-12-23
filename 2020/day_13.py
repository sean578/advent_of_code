from functools import reduce


def load_input(filename):
    raw = []
    for line in open(filename).readlines():
        raw.append(line.strip('\n'))

    busses = raw[1].split(',')
    busses[:] = [x if x != 'x' else 0 for x in busses]
    return [int(i) for i in busses]


def setup_equations(busses):
    n, b = [], []
    for i, bus in enumerate(busses):
        if bus != 0:
            n.append(-1*bus)
            b.append(i)
    return n, b


def modular_inverse(a, b):
    """ a^-1 (mod b) """

    a_reduced = a % b
    i = 1
    while True:
        if (i * a_reduced) % b == 1:
            break
        i += 1
    return i


def chinese_remainder_calc(n, b):
    """ Find x for set of equations "x mod bi = ni"
    Simple explanation: https://www.youtube.com/watch?v=zIFehsBHB8o&t=617s

    Args:
        n: ni as a list
        b: bi as a list
    """
    N_sum = abs(reduce((lambda x, y: x * y), n))
    N = [N_sum // i for i in n]
    mod_inv = [modular_inverse(x, y) for x, y in zip([abs(i) for i in N], [abs(i) for i in n])]
    t = [i*j*k for i, j, k in zip(b, N, mod_inv)]
    s = sum(t)
    return s % N_sum


if __name__ == '__main__':
    filename = 'day_13.txt'
    busses = load_input(filename)
    n, b = setup_equations(busses)
    answer = chinese_remainder_calc(n, b)

    print('answer part 2:', answer)
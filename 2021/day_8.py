import copy


def read_data(filename):
    return [line.strip().split(' | ') for line in open(filename).readlines()]


def get_segment_mapping(examples):

    # The actual mapping from digit to segments
    digit_to_segments = {
        0: {'A', 'B', 'C', 'E', 'F', 'G'},
        1: {'C', 'F'},
        2: {'A', 'C', 'D', 'E', 'G'},
        3: {'A', 'C', 'D', 'F', 'G'},
        4: {'B', 'C', 'D', 'F'},
        5: {'A', 'B', 'D', 'F', 'G'},
        6: {'A', 'B', 'D', 'E', 'F', 'G'},
        7: {'A', 'C', 'F'},
        8: {'A', 'B', 'C', 'D', 'E', 'F', 'G'},
        9: {'A', 'B', 'C', 'D', 'F', 'G'},
    }

    # How many times does each segment appear in the examples
    counts = {key: 0 for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}
    for e in examples:
        for s in e:
            counts[s] += 1

    # Hold the final mapping from lower case to upper case segment
    mapping = []
    mapping.append({key: None for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
    mapping.append({key: None for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
    mapping.append({key: None for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
    mapping.append({key: None for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})

    a_c = 0
    d_g = 0
    for key, value in counts.items():
        # If value appears n times in example then has to be one of the segments which appears n times in 0 - 9.
        if value == 6:
            mapping[0][key] = 'B'
            mapping[1][key] = 'B'
            mapping[2][key] = 'B'
            mapping[3][key] = 'B'
        elif value == 4:
            mapping[0][key] = 'E'
            mapping[1][key] = 'E'
            mapping[2][key] = 'E'
            mapping[3][key] = 'E'
        elif value == 9:
            mapping[0][key] = 'F'
            mapping[1][key] = 'F'
            mapping[2][key] = 'F'
            mapping[3][key] = 'F'
        elif value == 8:
            mapping[0][key] = ['A', 'C'][a_c]
            mapping[1][key] = ['A', 'C'][a_c]
            mapping[2][key] = ['C', 'A'][a_c]
            mapping[3][key] = ['C', 'A'][a_c]
            a_c += 1
        elif value == 7:
            mapping[0][key] = ['D', 'G'][d_g]
            mapping[1][key] = ['G', 'D'][d_g]
            mapping[2][key] = ['D', 'G'][d_g]
            mapping[3][key] = ['G', 'D'][d_g]
            d_g += 1
        else:
            print('Incorrect count')

    #Actual mapping for example
    # A : d, B : e, C : a, D : f, E : g, F : b, G : c

    # Get possible combinations of mapping
    # Need to try the 4 combinations of these (0, 1) until makes sense...
    for i in range(4):
        translated = []
        for e in examples:
            t = set()

            for s in e:
                t.add(mapping[i][s][0])

            translated.append(t)

        # Check if works
        works = True
        for t in translated:
            if t not in list(digit_to_segments.values()):
                works = False
        if works:
            correct_mapping = mapping[i]

    return correct_mapping


if __name__ == '__main__':
    data = read_data('day_8.txt')

    examples = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    example_input, example_output = examples.split(' | ')
    examples_input = example_input.split(' ')
    example_output = example_output.split(' ')

    correct_mapping = get_segment_mapping(examples_input)
    print(correct_mapping)
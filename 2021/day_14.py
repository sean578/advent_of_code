from collections import Counter

def read_data(filename):
    data = [line.strip() for line in open(filename).readlines()]
    template = data[0]
    insertions = [line.split(' -> ') for line in data[2:]]

    insertion_dict = {key: value for key, value in insertions}
    return template, insertion_dict


def create_pair_list(template):
    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i:i+2])
    return pairs


def get_insertions(pairs, insertion_dict):
    # Return letters to insert & insertion indicies
    insertions = []
    for i, pair in enumerate(pairs):
        if pair in insertion_dict:
            insertions.append([insertion_dict[pair], i])
    return insertions


def do_insertions(insertions, template):

    for i, insertion in enumerate(insertions):
        split = insertion[1] + i + 1
        template = template[:split] + insertion[0] + template[split:]

    return template


def get_answer(template):
    c = Counter(template)
    d = c.most_common()
    return d[0][1] - d[-1][1]


if __name__ == '__main__':
    template, insertion_dict = read_data('day_14.txt')
    # print('Template:', template)

    # for key, value in insertion_dict.items():
    #     print(key, value)

    # 1. Check all pairs, get pair index and replacement in list
    # 2. Do the insertions, use number of insertions to get correct location

    for step in range(10):
        print(step)
        pairs = create_pair_list(template)
        # print(pairs)
        insertions = get_insertions(pairs, insertion_dict)
        # print(insertions)
        template = do_insertions(insertions, template)
        # print('step', step+1, template)

    answer = get_answer(template)
    print('Answer:', answer)
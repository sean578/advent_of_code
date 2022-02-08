def read_data(filename):
    pass


def die_roll():
    value = 1
    while True:
        yield value
        value += 1
        if value > 100:
            value -= 100


def next_pos(current_pos, move):
    pos = current_pos + move
    pos = 1 + (pos - 1) % 10
    return pos


if __name__ == '__main__':
    # read_data('filename')

    # Die outputs: 1, 2, 3, ... 99, 100, 1, 2, ...
    die = die_roll()
    scores = {
        'p1': 0,
        'p2': 0
    }
    pos = {
        'p1': 1,
        'p2': 6
    }

    # Store number of times die rolled
    times_rolled = 0
    # First player with atleast 1000 points wins
    while scores['p1'] < 1000 and scores['p2'] < 1000:

        for player in scores:
            times_rolled += 3
            # Roll die 3 times and sum result
            die_sum = 0
            for _ in range(3):
                die_sum += next(die)
        
            # Move player sum moves
            pos[player] = next_pos(pos[player], die_sum)
            
            # Increase player score by final position
            # position 1, 2, ..., 9, 10, 1, 2,...
            scores[player] += pos[player]
            if scores[player] >= 1000:
                break
        
            # Complexity linear with number of moves
            # Roll: 3
            # Get position: 1
            # Increase player score: 1
            # Check if greater than 1000:

    # Get answer
    print(scores)
    print(pos)
    print(times_rolled)
    answer = min(scores.values()) * times_rolled
    print('Answer part 1:', answer)
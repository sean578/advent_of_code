if __name__ == '__main__':

    depths = [int(i.strip()) for i in open('day_1.txt').readlines()]

    num_increases = 0
    for i in range(len(depths)):
        if i > 2:
            if depths[i] > depths[i-3]:
                num_increases += 1

    print(num_increases)
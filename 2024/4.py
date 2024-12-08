def get_input():
    with open("4.txt") as f:
        a = [list(line.strip()) for line in f.readlines()]
    return a


def part_1(wordsearch):

    columns = len(wordsearch[0])
    rows = len(wordsearch)

    up = 0
    down = 0
    left = 0
    right = 0
    upright = 0
    downright = 0
    upleft = 0
    downleft = 0
    for y in range(rows):
        for x in range(columns):
            if wordsearch[y][x] == "X":
                # look to the right
                if x <= columns - 4:
                    if wordsearch[y][x] + wordsearch[y][x+1] + wordsearch[y][x+2] + wordsearch[y][x+3] == "XMAS":
                        right += 1
                # look to the left
                if x >= 3:
                    if wordsearch[y][x] + wordsearch[y][x-1] + wordsearch[y][x-2] + wordsearch[y][x-3] == "XMAS":
                        left += 1
                # look down
                if y <= rows - 4:
                    if wordsearch[y][x] + wordsearch[y+1][x] + wordsearch[y+2][x] + wordsearch[y+3][x] == "XMAS":
                        down += 1
                # look up
                if y >= 3:
                    if wordsearch[y][x] + wordsearch[y-1][x] + wordsearch[y-2][x] + wordsearch[y-3][x] == "XMAS":
                        up += 1
                # look diag down right
                if x <= columns - 4 and y <= rows - 4:
                    if wordsearch[y][x] + wordsearch[y+1][x+1] + wordsearch[y+2][x+2] + wordsearch[y+3][x+3] == "XMAS":
                        downright += 1
                # look diag up right
                if x <= columns - 4 and y >= 3:
                    if wordsearch[y][x] + wordsearch[y-1][x+1] + wordsearch[y-2][x+2] + wordsearch[y-3][x+3] == "XMAS":
                        upright += 1
                # look diag down left
                if x >= 3 and y <= rows - 4:
                    if wordsearch[y][x] + wordsearch[y+1][x-1] + wordsearch[y+2][x-2] + wordsearch[y+3][x-3] == "XMAS":
                        downleft += 1
                # look diag up left
                if x >= 3 and y >= 3:
                    if wordsearch[y][x] + wordsearch[y-1][x-1] + wordsearch[y-2][x-2] + wordsearch[y-3][x-3] == "XMAS":
                        upleft += 1

    return up + down + left + right + upright + downright + upleft + downleft


def part_2(wordsearch):

    columns = len(wordsearch[0])
    rows = len(wordsearch)

    count = 0
    for y in range(1, rows - 1):
        for x in range(1, columns - 1):
            if wordsearch[y][x] == "A":
                # check top-left to bottom-right
                if (wordsearch[y-1][x-1] == "M" and wordsearch[y+1][x+1] == "S") or (wordsearch[y-1][x-1] == "S" and wordsearch[y+1][x+1] == "M"):
                    # check top-right to bottom-left
                    if (wordsearch[y-1][x+1] == "M" and wordsearch[y+1][x-1] == "S") or (wordsearch[y-1][x+1] == "S" and wordsearch[y+1][x-1] == "M"):
                        count += 1

    return count


if __name__ == '__main__':
    wordsearch = get_input()

    print(part_1(wordsearch))
    print(part_2(wordsearch))

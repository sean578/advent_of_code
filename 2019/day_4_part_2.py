def check_repeating(num):
    num = str(num)
    ok = False
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            ok = True
    return ok


def check_increasing(num):
    num = str(num)
    ok = True
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            ok = False
    return ok


def check_only_2_repeating(num):
    num = str(num)
    num = [int(x) for x in str(num)]
    ok = False
    # edge case at beginning:
    if num[0] == num[1] and num[1] != num[2]:
        ok = True
    # edge case at end:
    if num[len(num)-1] == num[len(num)-2] and num[len(num)-1] != num[len(num)-3]:
        ok = True
    # the others
    for i in range(1, len(num)-2):
        if num[i] == num[i+1] and num[i] != num[i+2] and num[i] != num[i-1]:
            ok = True
    return ok


# print(check_only_2_repeating(222001))

start, stop = 153517, 630395

num_ok = 0
for i in range(start, stop+1):
    if check_increasing(i) and check_only_2_repeating(i):
        num_ok = num_ok + 1

print(num_ok)
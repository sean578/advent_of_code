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

start, stop = 153517, 630395

num_ok = 0

for i in range(start, stop+1):
    if check_repeating(i) and check_increasing(i):
        num_ok = num_ok + 1

print(num_ok)
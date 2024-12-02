lines = [x.strip() for x in open("2024/day02/data.in").readlines()]

# lines = [x.strip() for x in open("2024/day02/example.in").readlines()]


def decreasing_increasing_correctly(line, allowed_unsafe_no=1):
    line = line.split()
    x = list(map(int, line))
    up = x[0] < x[1] # increasing is true
    unsafe_cnt = 0
    last_value = 0
    for i in range(1, len(x)):
        diff = abs(int(x[i]) - int(x[i-1]))
        if (diff > 0 and diff < 4) and ((up and int(x[i]) > int(x[i-1])) or (not up and int(x[i]) < int(x[i-1]))):
            continue
        else:
            unsafe_cnt += 1
    
    return unsafe_cnt < 1


is_safe = 0
for x in lines:
    if decreasing_increasing_correctly(x):
        is_safe += 1
print(is_safe) # 572


def decreasing_increasing_correctly_bliep(line, allowed_unsafe_no=0):
    line = line.split()
    x = list(map(int, line))
    up = x[0] < x[1] # increasing is true
    unsafe_cnt = 0
    last_value = 0
    ignore = False
    for i in range(1, len(x)):
        diff = abs(x[i] - x[i-1])
        diff_ignore = abs(x[i] - x[i-2])
        if not ignore and ((diff > 0 and diff < 4) and ((up and x[i] > x[i-1]) or (not up and x[i]) < int(x[i-1]))):
            ignore = False
            continue
        # ignore previous value
        elif ignore and (diff_ignore > 0 and diff_ignore < 4) and ((up and x[i] > x[i-2]) or (not up and x[i] < x[i-2])):   
            ignore = False
            continue
        else:
            unsafe_cnt += 1
            if unsafe_cnt < allowed_unsafe_no:
                ignore = True

   
    return unsafe_cnt <= allowed_unsafe_no


is_safe = 0
for x in lines:
    # x = '40 37 37 36 32'
    if decreasing_increasing_correctly_bliep(x, 1):
        is_safe += 1



print(is_safe) # should be below next values <684


pass

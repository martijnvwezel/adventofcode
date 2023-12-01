from operator import methodcaller
# python -m timeit -n 100 -u msec "$(cat "day01/day01.py")"

filename = 'C:/git/adventofcode/2022/day01/data.in'
max_value = -1

elfs = sorted(map(lambda x: sum(map(int, x)) , map(methodcaller('split', '\n'), map(str.strip, open(filename).read().split('\n\n')))))

max_value = elfs[-1]
max_top3 =sum(elfs[-3:])


# max is 66616 elf 133
# 100 loops, best of 5: 3.98e-07 sec per loop

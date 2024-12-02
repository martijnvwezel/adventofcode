filename = '/mnt/c/git/adventofcode/2024/day01/data.in'
# filename = '/mnt/c/git/adventofcode/2024/day01/example.in'


# Read file
elfs = list(map(str.strip, open(filename).read().split('\n')))


elf = [list(map(int, line.split('   '))) for line in elfs]

a = [x[0] for x in elf]
b = [x[1] for x in elf]
a.sort()
b.sort()


# calculate diff between a and b
sumy = 0
for i in range(len(a)):
    sumy += abs(a[i] - b[i])

# assignment A
print(sumy)
print("Assignment A: ", sumy)

# assignment B
lookup = {x: b.count(x) for x in a}
result = sum(x * lookup[x] for x in a)

print("Assignment B: ", result)




pass
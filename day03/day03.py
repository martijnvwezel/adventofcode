import string


filename = 'C:/git/adventofcode/2022/day03/data.in'

total_score = 0
lookuptable = {}

i = 1
for va in string.ascii_lowercase + string.ascii_uppercase:
    lookuptable[va] = i
    i += 1


backpacks = open(filename).read().replace(' ', '').split()


for backp in backpacks:
    d1 = backp[:int(len(backp)/2)]
    d2 = backp[int(len(backp)/2):]

    commen = list(set(d1) & set(d2))[0]

    total_score += lookuptable[commen]


# print(total_score)

######################## challenge 2
total_score = 0


for i in range(0, len(backpacks), 3):
    b1 = backpacks[i]
    b2 = backpacks[i+1]
    b3 = backpacks[i+2]

    commen = list(set(b1) & set(b2) & set(b3))[0]

    total_score += lookuptable[commen]

# print(total_score)

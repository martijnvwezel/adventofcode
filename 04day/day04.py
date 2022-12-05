filename = 'C:/git/adventofcode/2022/04day/data.in'

total_score = 0


backpacks = open(filename).read().replace(' ', '').split()

for item in backpacks:
    elfs = item.split(",")

    e1 = list(map(int,elfs[0].split("-")))
    e2 = list(map(int,elfs[1].split("-")))


    a = (e2[0] <= e1[0] and e2[1] >= e1[1]) or  \
          e1[0] <= e2[0] and e1[1] >= e2[1]


    total_score += int(a)


print(f"{total_score}")


#### assignment 2
filename = 'C:/git/adventofcode/2022/04day/data.in'

total_score = 0

for item in backpacks:
    elfs = item.split(",")

    e1 = list(map(int,elfs[0].split("-")))
    e2 = list(map(int,elfs[1].split("-")))

    a = e1[0] >= e2[0] and  e1[0] <= e2[1] or \
        e1[1] >= e2[0] and  e1[1] <= e2[1] or \
        e2[0] >= e1[0] and  e2[0] <= e1[1] or \
        e2[1] >= e1[0] and  e2[1] <= e1[1]

    total_score += int(a)


print(f"{total_score}")






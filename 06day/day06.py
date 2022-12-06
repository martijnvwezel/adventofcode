filename = 'C:/git/adventofcode/2022/06day/data.in'
data = open(filename).read()

after_msg = 4

total_score = 0
after_msg -= 1
for i in range(0, len(data)):
    total_score += 1
    if i < after_msg:
        continue

    p = data[i-after_msg:i+1]

    if len(set(p)) == after_msg+1:
        print(f"total_score: {total_score}")
        break

# fase 2
after_msg = 14

total_score = 0
after_msg -= 1
for i in range(0, len(data)):
    total_score += 1
    if i < after_msg:
        continue

    p = data[i-after_msg:i+1]

    if len(set(p)) == after_msg+1:
        print(f"total_score: {total_score}")
        break

pass

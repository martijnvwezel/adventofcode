filename = 'C:/git/adventofcode/2022/day06/data.in'
data = open(filename).read()

after_msg = 4

for i in range(0, len(data)):
    p = data[i:i+after_msg]
    if len(set(p)) == after_msg:
        print(f"total_score: {i+after_msg}")
        break

# fase 2
after_msg = 14

for i in range(0, len(data)):
    p = data[i:i+after_msg]
    if len(set(p)) == after_msg:
        print(f"total_score: {i+after_msg}")
        break

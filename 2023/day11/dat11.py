import pandas as pd

lines = [x.strip() for x in open("2023/day11/data.in").readlines()]
 
exp = []
for line in lines:
    if line == '.'*len(line):
        exp.append(line)
    exp.append(line)

exp = pd.DataFrame(map(list, exp))


# check if columns is only filled with dots
for col in exp.columns:
    if exp[col].value_counts().get('.', 0) == len(exp):
        # insert column before the current column
        exp.insert(col, col, '.')

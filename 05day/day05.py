#         [G]         [D]     [Q]
# [P]     [T]         [L] [M] [Z]
# [Z] [Z] [C]         [Z] [G] [W]
# [M] [B] [F]         [P] [C] [H] [N]
# [T] [S] [R]     [H] [W] [R] [L] [W]
# [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
# [C] [N] [H] [R] [N] [H] [D] [J] [Q]
# [N] [D] [M] [G] [Z] [F] [W] [S] [S]
#  1   2   3   4   5   6   7   8   9

filename = 'data.in'
total_score = 0

stapels = [ ['Antwoord: '],
            ['N','C','R','T','M','Z','P'],
            ['D','N','T','S','B','Z'],
            ['M','H','Q','R','F','C','T','G'],
            ['G','R','Z'],
            ['Z','N','R','H'],
            ['F','H','S','W','P','Z','L','D'],
            ['W','D','Z','R','C','G','M'],
            ['S','J','F','L','H','W','Z','Q'],
            ['S','Q','P','W','N']]

from operator import methodcaller

data = list(map(methodcaller("split"," " ), open(filename).read().split('\n')))




for todo in data:

    amount_to_move = int(todo[1])
    from_list = int(todo[3])
    to_list = int(todo[5])


    # Set the from list correct
    temp = stapels[from_list][-amount_to_move:]
    stapels[from_list] = stapels[from_list][:-amount_to_move]


    # * Enable for assignment 5a
    # temp.reverse()

    # set the to list correct
    stapels[to_list] = stapels[to_list] + temp

ans = ""
for i in stapels:
    ans = ans + i[-1]

print(ans)


# its not MWWQZFNJ
# STHGRZZFR
# STHGRZZF
#
# Antwoord: RTGWZTHLD







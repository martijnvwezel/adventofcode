filename = '/mnt/c/git/adventofcode/2023/day02/data.in'


elfs = list(map(str.strip, open(filename).read().split('\n')))

# example = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
# ]
# elfs = example

thresholds = {'blue': 14, 'red': 12, 'green': 13}

sum = 0
for bags in elfs:
    games = bags.split(':')[0].split(' ')[1]
    all_bags = bags.split(':')[1].split(';')

    threshold_reached = False
    for item in all_bags: 
        bag = item.strip().split(',')

        for it in bag:
            if it == '':
                continue
            no = int(it.strip().split(' ')[0])
            color = it.strip().split(' ')[1]
            if no > thresholds[color]:
                threshold_reached = True
    
    if not threshold_reached:
        sum += int(games)

print(sum)


# assignment 2
sum = 0

for bags in elfs:
    bags = bags.split(':')[1].replace(';', ',').split(', ')

    maxi = {'blue': 0, 'red': 0, 'green': 0}
    for item in bags:
        no = int(item.strip().split(' ')[0])
        color = item.strip().split(' ')[1]

        if maxi[color] < no: 
            maxi[color] = no

    sum += maxi['blue'] * maxi['red'] * maxi['green']

print(sum)
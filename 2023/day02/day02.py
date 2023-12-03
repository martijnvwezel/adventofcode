filename = '/mnt/c/git/adventofcode/2023/day02/data.in'

import time 


elfs = list(map(str.strip, open(filename).read().split('\n')))


start_time = time.time()

for i in range(1000):
   

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
        [games, all_bags] = bags.split(':')
        games = games.split()[1]   

        threshold_reached = False
        for item in all_bags.split(';'): 

            # * deze functie vervangen met 
            for it in item.split(', '):
                [no, color] = it.strip().split(' ')
                threshold_reached = threshold_reached or int(no) > thresholds[color]
            
            
            # * Deze functie
            # threshold_reached_2 = any([int(no) > thresholds[color] for no, color in (it.strip().split(' ') for it in item.split(', '))]+[False])

        # if threshold_reached != threshold_reached_2:
        #     print([int(no) > thresholds[color] for no, color in (it.strip().split(' ') for it in bag)]+[False])

        if not threshold_reached:
            sum += int(games)


print(f"time : { (time.time()-start_time)/1000}")


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
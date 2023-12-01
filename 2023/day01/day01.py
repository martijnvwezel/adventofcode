from operator import methodcaller
import re
filename = '/mnt/c/git/adventofcode/2023/day01/data.in'


elfs = list(map(str.strip, open(filename).read().split('\n')))





sum = 0
for row in elfs:

    numbers_only = re.sub(r'[^0-9]', '', row)
    sum += int(numbers_only[0] + numbers_only[-1])

print(sum)





### assignment 2


number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


sum = 0
for row in elfs:
    output_string = row

    for nu in number_dict:
        output_string = output_string.replace(nu, str(number_dict[nu]))

    numbers_only = re.sub(r'[^0-9]', '', output_string)

    sum += int(numbers_only[0] + numbers_only[-1])


    print(row, "  --   ", output_string,"  ----   ",int(numbers_only[0] + numbers_only[-1]))


print(sum)
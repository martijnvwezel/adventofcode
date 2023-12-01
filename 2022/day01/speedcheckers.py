import os
from time import time
import pandas as pd


filename = 'C:/git/adventofcode/2022/01day/data.in'
print(f'File Size is {os.stat(filename).st_size / (1024)} KB')


start = time()


for i in range(1000):
    txt_file = open(filename)
    count = 0
    data = []
    for line in txt_file:
        # we can process file line by line here, for simplicity I am taking count of lines
        data = data + [line]

    txt_file.close()
print(time()-start)

start = time()
for i in range(1000):
    data = pd.read_fwf(filename)



print(time()-start)


# data = pd.read_fwf(filename)

data = pd.read_csv(filename, header=None, skip_blank_lines=True, nrows=2250,memory_map=True,verbose=False)


def find_max_elf():
    # * The time difference is: 0.0007316996343433857
    elf = -1
    max_value = -1
    idx = 1
    with open(filename) as f:
        alist = [int(line.rstrip() or 0) for line in f]
        alist = [int(line.rstrip() or 0) for line in f.readlines().split('\n\n')]

        total = 0
        for line in f:
            v = line.rstrip()
            if v != '':
                total = total + int(v)
            else:
                if total > max_value:
                    elf = idx
                    max_value = total
                total = 0
                idx += 1

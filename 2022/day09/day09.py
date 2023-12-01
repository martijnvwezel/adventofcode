from operator import methodcaller

filename = 'data.in'
total_score = 0
file_structure = {}
map_depth = []
dir_to_See = ''

data = list(map(methodcaller("split", " "), open(filename).read().split('\n')))

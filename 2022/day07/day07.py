from operator import methodcaller

filename = 'data.in'
total_score = 0
file_structure = {}
map_depth = []
dir_to_See = ''

data = list(map(methodcaller("split", " "), open(filename).read().split('\n')))

for todo in data:
    if '$' == todo[0]:
        if 'cd' == todo[1]:
            if '/' == todo[2]:
                map_depth = []
            elif '..' == todo[2]:
                map_depth = map_depth[:-1]
            else:
                map_depth = map_depth + [todo[2]]
        elif 'ls' == todo[1]:
            dir_to_See = '' if len(todo) == 2 else todo[2]  # handle ls <somehting>
            if ''.join(map_depth) not in file_structure:
                filepath = ''.join(map_depth)
                filepath = filepath if len(filepath) > 0 else ' '
                file_structure[filepath] = 0
            if ''.join(map_depth)+dir_to_See not in file_structure:
                filepath = ''.join(map_depth) + dir_to_See
                filepath = filepath if len(filepath) > 0 else ' '
                file_structure[filepath] = 0

    else:
        if 'dir' != todo[0]:
            filepath = ''.join(map_depth) + dir_to_See
            filepath = filepath if len(filepath) > 0 else ' '
            file_structure[filepath] += int(todo[0])

total_disk_space, needed_space = 70000000, 30000000
total_disk_size_files = 0
for dir in file_structure:
    total_disk_size_files += file_structure[dir]

remove_size = needed_space - (total_disk_space-total_disk_size_files)
# print(f"Needed amount of directory space to delete {remove_size}")

part_two = {}
for dir in file_structure:
    size_of_folder = 0
    for a in file_structure:
        if dir in a:
            size_of_folder += file_structure[a]

    if size_of_folder < 100000:
        total_score += size_of_folder

    if size_of_folder >= remove_size:
        part_two[dir] = size_of_folder

print(f"Total file size less than 100000: {total_score}")
size = [part_two[a] for a in part_two]
size.sort()
print(f"smalles size that can be removed: {size[0]}")


filename = 'C:/git/adventofcode/2022/day02/data.in'

# rock -> A/x -> 1 punt
# paper -> B/y -> 2 punt
# sciss -> C/z -> 3 punt

# win -> 6 + A/B/C
# los -> 0 + A/B/C
# dra -> 3

x,y,z = 1,2,3
w,d,l = 6,3,0
lookuptable   = {
    'AX': d+x,
    'AY': w+y,
    'AZ': l+z,
    'BX': l+x,
    'BY': d+y,
    'BZ': w+z,
    'CX': w+x,
    'CY': l+y,
    'CZ': d+z
}


print(sum(list(map(lambda x: lookuptable[x],open(filename).read().replace(' ','').split()))))

# Now x,y,z, have a different meaning
# x = loose
# y = draw
# z = win
r,p,s = 1,2,3
lookuptable2   = {
    'AX': l+s,
    'AY': d+r,
    'AZ': w+p,
    'BX': l+r,
    'BY': d+p,
    'BZ': w+s,
    'CX': l+p,
    'CY': d+s,
    'CZ': w+r
}
print(lookuptable2)

print(sum(list(map(lambda x: lookuptable2[x],open(filename).read().replace(' ','').split()))))


import pandas as pd



filename = '/mnt/c/git/adventofcode/2023/day03/data.in'



elfs = list(map(str.strip, open(filename).read().split('\n')))

example = [    
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
    "...$.&....",
    # "467*114..."
]
# elfs = example


# elfs = elfs[130:]

# Create a DataFrame from the grid
df = pd.DataFrame([list(row) for row in elfs])

def is_symbols(char) -> bool:
    return char is not None and not (char.isdigit() or char.isalpha() or char == '.')

def validate_star_around(df, x, y) -> bool:
    try: 
        return  df.iloc[x, y] is not None and df.iloc[x, y] == '*'
    except: 
        return False

def validate_is_digit(df, x, y) -> bool:
    try: 
        return df.iloc[x, y].isdigit() and df.iloc[x, y] != '.'
    except: 
        return False


def check_symbol_around(df , i , j ) -> bool :
    # row_b = validate_star_around(df, i-1, j-1) or validate_star_around(df, i-1, j)  or validate_star_around(df, i-1, j+1)
    row_c = validate_star_around(df, i,   j+1)
    row_n = validate_star_around(df, i+1, j-1) or validate_star_around(df, i+1, j)  or validate_star_around(df, i+1, j+1)
    return  row_c or row_n



def find_compleet_digit(row, index) -> str:
    # find left value of that 
    # correct for not starting at a . instead of 1 for example .11
    i = index
    value =  '' 
    # find the start of the number
    while i >= 0 and row[i].isdigit():
        i -= 1

    i += 1
    # ........*328...............&..........................144.*.......
    while i < len(row) and row[i].isdigit():
        value += row[i]
        i += 1

    return value

    

    # while  validate_is_digit(row, )

def find_connected_value(df , i , j):
    # 0 is not found
    # not 0 is linked 
    # Search area
    # | 0 0 1 |
    # | 1 * 1 |
    # | 1 1 1 |
    digit_value = ''
    
    # # validate position 3
    # k = 0
    # while validate_is_digit(df, i-1, j+1+k):
    #     digit_value += df.iloc[i-1, j+1+k]
    #     k += 1
    # if len(digit_value) > 0:
    #     return digit_value
    
    
    # validate position 6
    k = 0
    while validate_is_digit(df, i, j+1+k):
        digit_value += df.iloc[i, j+1+k]
        k += 1
    if len(digit_value) > 0:
        return digit_value
    
    # validate position 4 special one 
    k = 1
    while validate_is_digit(df, i, j-k):
        digit_value = df.iloc[i, j-k] + digit_value
        k += 1
    if len(digit_value) > 0:
        return digit_value



    # validate position around , does not work with >2 values around the *    
    if validate_is_digit(df, i+1, j-1):
        return find_compleet_digit(row=list(df.iloc[i+1]), index=j-1)

    if validate_is_digit(df, i+1, j):
        return find_compleet_digit(row=list(df.iloc[i+1]), index=j)

    if validate_is_digit(df, i+1, j+1):
        return find_compleet_digit(row=list(df.iloc[i+1]), index=j+1)

     # find a value around the start
    return ''

def check_special_symbol(df , i, j):
    special_number = ''
    print(df.iloc[i, j])
    if validate_star_around(df, i,   j+1):
        special_number = find_connected_value(df, i,   j+1)
        df.iloc[i, j+1] = '.'

    if special_number == '' and validate_star_around(df, i+1, j-1):
        special_number = find_connected_value(df, i+1, j-1)
        df.iloc[i+1, j-1] = '.'

    if special_number == '' and validate_star_around(df, i+1, j)  :
        special_number = find_connected_value(df, i+1, j)  
        df.iloc[i+1, j] = '.'

    if special_number == '' and validate_star_around(df, i+1, j+1):
        special_number = find_connected_value(df, i+1, j+1)
        df.iloc[i+1, j+1] = '.'

    return df , special_number





sum = int(0) # make sure it 64-bit
building_no = ''
special_symbol_value = ''
er = 0
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        value = df.iloc[i, j]

        if value == '.' or is_symbols(value):
            if len(building_no) > 0 and len(special_symbol_value) > 0 :
                print(f"{len(special_symbol_value)> 0} startno = {building_no} and {special_symbol_value}")     
                sum += int(building_no) *  int(special_symbol_value)

            # Reset search
            building_no = ''
            special_symbol_value = ''
            continue
        
        # is this near another symbol
        if check_symbol_around(df , i , j ):
            symbol_found = True

            # check edge case  * and ignore 


            df , f_value = check_special_symbol(df , i, j)
            # print(f_value)
            special_symbol_value = f_value




        building_no += value    

print(sum)
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================
# not 73948798, 76681305 too low, 61935861 not right, not right 61935861


# assignment 2
sum = int(0) # make sure it 64-bit
building_no = ''
special_symbol_value = ''
symbol_found = False
er = 0
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        value = df.iloc[i, j]

        if value == '.' or is_symbols(value):
            if len(building_no) > 0 and symbol_found:
                # print(f"er: {er}")
                # if er > 1:
                    # raise Exception("Cannot deal with multiple * around int")
                # print(building_no)
                print(f"{len(special_symbol_value)> 0} startno = {building_no} and {special_symbol_value}")
                if len(special_symbol_value) > 0:                   
                    sum += int(building_no) *  int(special_symbol_value)
                    # print(f"startno = {building_no} and {special_symbol_value}")

            # Reset search
            building_no = ''
            symbol_found = False
            special_symbol_value = ''
            er = 0
            continue
        
        f_value = False
        # is this near another symbol
        if check_symbol_around(df , i , j ):
            symbol_found = True

            # check edge case  * and ignore 
            if check_symbol_around_ignore_star(df ,i ,j):
                er += 1

            df , f_value = check_special_symbol(df , i, j)
            # print(f_value)
            special_symbol_value = f_value




        building_no += value    

# print(''.join(list(df.iloc[0, : ])))
# print(''.join(list(df.iloc[1, : ])))
# print(''.join(list(df.iloc[2, : ])))
print(sum)

# not 73948798, 76681305 too low, 61935861 not right, not right 61935861



from itertools import groupby
from math import prod
from operator import itemgetter
from re import finditer,search,sub

#(f:=open(0).read()) and (N:=f.find('\n')+2) and (s:='..'*N+sub('\n','..',f)+'..'*N) and print(sum(int(x[0]) for x in finditer(r'\d+',s) if any(search(r'[^0-9.]',s[i+x.start()-1:i+x.end()+1]) for i in [-N,0,N])))

# (f:=open(filename).read()) and (N:=f.find('\n')+2) and (s:='..'*N+sub('\n','..',f)+'..'*N) and print(sum(t:=[*g]) and len(t)==2 and t[0][1]*t[1][1] and (print(f"{ t[0][1]}{t[1][1]}")) for _,g in groupby(sorted((j,int(x[0])) for x in finditer(r'\d+',s) for i in [-N,0,N] for j in range(i+x.start()-1,i+x.end()+1) if s[j]=='*'),itemgetter(0)))


# file_content = open(filename).read()

# # Find the position of the first newline character
# N = file_content.find('\n') + 2

# # Create a modified string for easier processing
# s = '..' * N + sub('\n', '..', file_content) + '..' * N

# # Group and count the occurrences of '*' around numbers

# for _, g in groupby(
#     sorted(
#         (j, int(x[0])) 
#         for x in finditer(r'\d+', s) 
#         for i in [-N, 0, N] 
#         for j in range(i + x.start() - 1, i + x.end() + 1) 
#         if s[j] == '*'
#     ), itemgetter(0)
# ) 
# if (
#     sum(t := [*g]) 
#     and len(t) == 2 
#     and t[0][1] * t[1][1]
# )

# # Print the result (sum of t)
# print("Sum of t:", sum(result))


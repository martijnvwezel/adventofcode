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
    ".664.598.."
]
# elfs = example


# elfs = elfs[130:]

# Create a DataFrame from the grid
df = pd.DataFrame([list(row) for row in elfs])

def is_symbols(char) -> bool:
    return char is not None and not (char.isdigit() or char.isalpha() or char == '.')

def validate_is_symbol(df, x, y) -> bool:
    try: 
        return is_symbols(df.iloc[x, y])
    except: 
        return False

def validate_is_digit(df, x, y) -> bool:
    try: 
        return df.iloc[x, y].isdigit()
    except: 
        return False


def check_symbol_around(df , i , j ) -> bool :
    row_b = validate_is_symbol(df, i-1, j-1) or validate_is_symbol(df, i-1, j)  or validate_is_symbol(df, i-1, j+1)
    row_c = validate_is_symbol(df, i  , j-1) or False                           or validate_is_symbol(df, i,   j+1)
    row_n = validate_is_symbol(df, i+1, j-1) or validate_is_symbol(df, i+1, j)  or validate_is_symbol(df, i+1, j+1)
    return row_b or row_c or row_n


def validate_is_symbol_ignore_star(df, x, y) -> bool:
    try: 
        char = df.iloc[x, y]
        return char is not None and not (char.isdigit() or char.isalpha() or char == '.' or char == '*')
    except: 
        return False
def check_symbol_around_ignore_star(df , i , j ) -> bool :
    row_b = validate_is_symbol_ignore_star(df, i-1, j-1) or validate_is_symbol_ignore_star(df, i-1, j)  or validate_is_symbol_ignore_star(df, i-1, j+1)
    row_c = validate_is_symbol_ignore_star(df, i  , j-1) or False                                       or validate_is_symbol_ignore_star(df, i,   j+1)
    row_n = validate_is_symbol_ignore_star(df, i+1, j-1) or validate_is_symbol_ignore_star(df, i+1, j)  or validate_is_symbol_ignore_star(df, i+1, j+1)
    return row_b or row_c or row_n

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

def find_connected_value(df , i , j, not_ignore=True):
    # 0 is not found
    # not 0 is linked 
    # Search area
    # | 0 0 0 |
    # | s * 1 |
    # | 1 1 1 |
    digit_value = ''
    
    # validate position 6
    k = 0
    while validate_is_digit(df, i, j+k):
        digit_value += df.iloc[i, j+k]
        k += 1
    if len(digit_value) > 0:
        return digit_value
    

    # validate position 4 special one 
    if not_ignore: 
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
    row_b   = 0 
    special = '.'
    special_number = '' # the founded number will be placed here
    # found = validate_is_symbol(df, i-1, j-1)  and df.iloc[i-1, j-1] == '*'
    # if found:
    #     row_b += 1
    #     special_number = find_connected_value(df, i-1, j-1)
    #     df.iloc[i-1, j-1] = special

    # found = validate_is_symbol(df, i-1, j)    and df.iloc[i-1, j] == '*'
    # if found:
    #     row_b += 1
    #     special_number = find_connected_value(df, i-1, j)  
    #     df.iloc[i-1, j] = special

    # found = validate_is_symbol(df, i-1, j+1)  and df.iloc[i-1, j+1] == '*'
    # if found:
    #     row_b += 1
    #     special_number = find_connected_value(df, i-1, j+1)
    #     df.iloc[i-1, j+1] = special

    # found = validate_is_symbol(df, i  , j-1)  and df.iloc[i  , j-1] == '*'
    # if found:
    #     row_b += 1
    #     special_number = find_connected_value(df, i  , j-1,  not_ignore = False)
    #     df.iloc[i  , j-1] = special

    found = validate_is_symbol(df, i,   j+1, )  and df.iloc[i, j+1] == '*'
    if found:
        row_b += 1
        special_number = find_connected_value(df, i,   j+1, not_ignore = False)
        df.iloc[i,   j+1] = special

    found = validate_is_symbol(df, i+1, j-1)  and df.iloc[i+1, j-1] == '*'
    if found:
        row_b += 1
        special_number = find_connected_value(df, i+1, j-1)
        df.iloc[i+1, j-1] = special

    found = validate_is_symbol(df, i+1, j)    and df.iloc[i+1, j] == '*'
    if found:
        row_b += 1
        special_number = find_connected_value(df, i+1, j)  
        df.iloc[i+1, j] = special

    found = validate_is_symbol(df, i+1, j+1)  and df.iloc[i+1, j+1] == '*'
    if found:
        row_b += 1
        special_number = find_connected_value(df, i+1, j+1)
        df.iloc[i+1, j+1] = special

    # if len(special_number) > 0:
    #     print(special_number)

    if row_b > 1:
        raise Exception("This example ignored multiple * operators around a value..")
    return df , (special_number if row_b > 0  else '')


# assignment 1
sum = 0 
building_no = ''
symbol_found = False
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        value = df.iloc[i, j]

        if value == '.' or is_symbols(value):
            if len(building_no) > 0 and symbol_found:
                sum += int(building_no)
            # Reset search
            building_no = ''
            symbol_found = False
            continue
        
        building_no += value

        # is this near another symbol
        if check_symbol_around(df , i , j ):
            symbol_found = True

print(f"The sum assignment 1: {sum}")

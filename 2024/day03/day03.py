
import string

alphabet = set(string.ascii_lowercase + '[](')


lines = [x.strip() for x in open("2024/day03/data.in").readlines()]

# lines = [x.strip() for x in open("2024/day03/example.in").readlines()]

muls = []
enable = True
for x in lines:
    stop_pos = 0
    x = x.replace(" ", "")
    while True:
        start_pos = stop_pos
        start_pos = x.find("mul(", start_pos)
        if start_pos == -1:
            print(x[stop_pos:])
            break

        stop_pos = x.find(")", start_pos)
        ss = x[start_pos+4:stop_pos].lower()

        if set(ss).issubset(set('0123456789,')) and not( ":" in ss):
            muls.append(x[start_pos+4:stop_pos])

        stop_pos = start_pos + 1


sumy = 0
for x in muls:
    ss = x.split(",")
    print(f"{x} - {ss}")
    sumy += int(ss[0]) * int(ss[1])

print(f"total sum A: {sumy}") # not those -> 31872341 , 32565145
pass
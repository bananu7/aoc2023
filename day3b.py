import re
from collections import defaultdict

def is_symbol(c):
    return c == '*'

def touches_char(lines, x, y):
    offsets = [
        (-1,-1),
        ( 0,-1),
        ( 1,-1),
        ( 1, 0),
        ( 1, 1),
        ( 0, 1),
        (-1, 1),
        (-1, 0),
    ]
    for o in offsets:
        yy = y + o[0]
        xx = x + o[1]
        if yy >= len(lines):
            continue
        if y < 0:
            continue

        if xx >= len(lines[yy]):
            continue
        if xx < 0:
            continue

        if is_symbol(lines[yy][xx]):
            return (xx,yy)
    return False

stars = defaultdict(list)
def mark_touching_stars(lines, row, a, b, intnum):
    xys = {}
    for x in range(a,b):
        mxy = touches_char(lines, x, row)
        if mxy:
            xys[mxy] = True
    for xy in xys:
        stars[xy].append(intnum)

with open("input3.txt") as file:
    lines = [line.rstrip() for line in file]

    for row, line in enumerate(lines):
        for num in re.finditer("[0-9]+", line):
            (a,b) = num.span()
            mark_touching_stars(lines, row, a, b, int(num.group()))

# final compute

print(stars)

sum = 0
for star in stars:
    nums = stars[star]
    if len(nums) != 2:
        continue
    sum += nums[0] * nums[1]

print(sum)


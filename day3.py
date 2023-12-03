import re

def is_symbol(c):
    return c != '.' and not c.isalnum()

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
            return True

def touches_symbol(lines, row, a, b):
    for x in range(a,b):
        if touches_char(lines, x, row):
            return True
    return False

sum = 0

with open("input3.txt") as file:
    lines = [line.rstrip() for line in file]

    for row, line in enumerate(lines):
        for num in re.finditer("[0-9]+", line):
            (a,b) = num.span()
            if touches_symbol(lines, row, a, b):
                sum += int(num.group())

print(sum)


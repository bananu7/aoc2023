file1 = open("input_1.txt", "r")
lines = file1.readlines()

count = 0

digs = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"],
]


def fixfirst(line):
    while True:
        if line[0].isdigit():
            return line

        for d in digs:
            if line.startswith(d[0]):
                return line.replace(d[0], d[1], 1)

        line = line[1:]


def fixlast(line):
    while True:
        if line[-1].isdigit():
            return line

        for d in digs:
            if line.endswith(d[0]):
                # return line.replace(d[0], d[1], 1)
                return d[1].join(line.rsplit(d[0], 1))

        line = line[0:-1]


def fix(line):
    return fixlast(fixfirst(line))


for line in lines:
    line = fix(line)

    print(line)

    first = True
    last = 0
    code = 0
    for c in line:
        if c.isdigit():
            if first:
                code += int(c) * 10
                first = False
            last = int(c)
    code += last
    print(code)
    count += code
    code = 0

print(count)

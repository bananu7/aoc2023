file1 = open("input_1.txt", "r")
lines = file1.readlines()

count = 0

for line in lines:
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

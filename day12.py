def group(springs):
    groups = []
    inside = springs[0] == "#"
    count = 0
    for i in range(0, len(springs)):
        if inside:
            if springs[i] == "#":
                count += 1
            else:
                groups.append(count)
                count = 0
                inside = False
        else:
            if springs[i] == "#":
                count = 1
                inside = True
            else:
                continue
    if inside:
        groups.append(count)
    return groups


def check(springs, nums):
    return group(springs) == nums


def generate(num, bit_locs, springs_template):
    springs = list(springs_template)
    for i in range(0, len(bit_locs)):
        if num & (2**i):
            springs[bit_locs[i]] = "#"
        else:
            springs[bit_locs[i]] = "."
    return "".join(springs)


def brute_count(springs, nums):
    bit_locs = []
    for i in range(0, len(springs)):
        if springs[i] == "?":
            bit_locs.append(i)

    count = 0
    m = 2 ** len(bit_locs)
    print("Generating...", m)
    for n in range(0, m):
        springs_filled = generate(n, bit_locs, springs)
        # print(springs_filled, group(springs_filled))
        if check(springs_filled, nums):
            count += 1
    print("---")
    return count


def main():
    file = open("input12.txt", "r")
    lines = file.readlines()

    sum = 0
    for line in lines:
        [springs, num_str] = line.strip().split(" ")
        nums = list(map(int, num_str.split(",")))

        print()
        print(springs, nums)
        count = brute_count(springs, nums)
        print(count)
        sum += count
    print(sum)


main()

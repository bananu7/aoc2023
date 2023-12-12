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
    #print("Generating...", m)
    for n in range(0, m):
        springs_filled = generate(n, bit_locs, springs)
        # print(springs_filled, group(springs_filled))
        if check(springs_filled, nums):
            count += 1
    #print("---")
    return count

### p2

def find_first_group(springs):
    start = None
    ln = 0
    for i in range(0, len(springs)):
        if start == None:
            if springs[i] == ".":
                continue
            else:
                start = i
                ln = 1
        else:
            if springs[i] == "?" or springs[i] == "#":
                ln += 1
            else:
                return start, ln

    return start, ln


def tree_count(springs, nums, tab = 0):
    print("\t" * tab, "rawentry", springs, nums)
    if len(nums) == 0:
        return 1

    if len(springs) == 0:
        return 0

    num = nums[0]

    # generate all possible locations for that num
    # - find the first group where it would fit
    # - if no groups return 0
    # - if the first group is too small then return 0
    # - else generate all fitments for that group 
    # recurse down and repeat with the cut out parts and rest of the nums

    x, ln = find_first_group(springs)
    if x == None:
        print("no first group")
        return 0

    if ln < num:
        print("first group",ln,"smaller than num",num)
        return 0

    springs = springs[x:] # cut off the starting dots
    print("\t" * tab, "entry", springs, x, ln, nums)

    mincut = min(num + 1, len(springs)) # at least num
    maxcut = min(ln + 1, len(springs)) # at most entire group and one dot

    cuts = list(range(mincut, maxcut+1))

    def valid(cut):
        if cut > len(springs):
            return False

        if cut == len(springs):
            return True

        # need to check if it can have a dot right after
        return springs[cut-1] in [".", "?"] and cut > num

    print("\t" * tab, "cuts", cuts)
    cuts = list(filter(valid, cuts))
    print("\t" * tab, "vcuts", cuts)

    options = list(map(lambda cut: springs[cut:], cuts))

    print("\t" * tab, "options", options)

    counts = list(map(lambda option: tree_count(option, nums[1:], tab+1), options))

    print("\t" * tab, springs, "xln", nums, x, ln)
    print("\t" * tab, "->", options, counts)

    return sum(counts)
###

'''
1
4
1
1
4
10
21
'''

def main():
    file = open("input12_test.txt", "r")
    lines = file.readlines()

    sum = 0
    for line in lines:
        [springs, num_str] = line.strip().split(" ")
        nums = list(map(int, num_str.split(",")))

        #print()
        #print(springs, nums)
        #count = brute_count(springs, nums)
        count = tree_count(springs, nums)
        print(count)
        sum += count
    print(sum)


main()

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

def find_first_group_of_minimum(springs, num):
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
                if ln >= num:
                    return start, ln
                else:
                    start = None
                    ln = 0

    return start, ln

def tree_count(springs, nums, tab = 0):
    def debug(*args):
        print("\t" * tab, *args)

    debug("rawentry", springs, nums)
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

    x, ln = find_first_group_of_minimum(springs, num)
    if x == None:
        debug("no first group")
        return 0

    if ln < num:
        debug("first group",ln,"smaller than num",num)
        return 0

    springs = springs[x:] # cut off the starting dots
    debug("entry", springs, x, ln, nums)

    minoff = 0
    maxoff = len(springs) - num # at most entire group and one dot

    offs = list(range(minoff, maxoff+1))
    valid_offs = []

    def valid(off):
        if off > len(springs):
            debug("cut < len", off, len(springs), springs)
            return False

        if off+num == len(springs):
            return True

        for i in range(0, off - num):
            if springs[i] == "#":
                debug(off, "left")
                return False

        # need to check if it can have a dot at the last element of the cut
        return springs[off+num] in [".", "?"]

    debug("offs", offs)
    offs = list(filter(valid, offs))
    debug("voffs", offs, num)
    cuts = map(lambda off: off+num, offs)

    options = list(map(lambda off: springs[(num+off+1):], offs))
    options = list(filter(lambda opt: len(opt) == 0 or opt[0] in ["?", "#"], options)) # filter starting dots

    debug("options", options)

    counts = list(map(lambda option: tree_count(option, nums[1:], tab+1), options))

    debug(springs, "xln", nums, x, ln)
    debug("->", options, counts, "\n")

    s = sum(counts)
    debug(s)
    return sum(counts)
###

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


def test():
    assert tree_count("???.###", [1,1,3]) == 1
    assert tree_count(".??..??...?##.", [1,1,3]) == 4
    assert tree_count("?#?#?#?#?#?#?#?", [1,3,1,6]) == 1
    assert tree_count("????.#...#...", [4,1,1]) == 1
    assert tree_count("????.######..#####.", [1,6,5]) == 4
    assert tree_count("?###????????", [3,2,1]) == 10

test()
#main()


 

 

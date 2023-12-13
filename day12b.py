import re

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


def find_first_hash(springs):
    for i in range(0, len(springs)):
        if springs[i] == "#":
            return i
    return None


def tree_count(springs, nums, tab = 0):
    springs = re.sub(r'\.+', '.', springs)
    def debug(*args):
        #print("\t" * tab, *args)
        pass

    debug("tree_count", springs, nums)

    if len(nums) == 0:
        if find_first_hash(springs) == None:
            return 1
        else:
            return 0

    if len(springs) == 0:
        return 0

    num = nums[0]

    # generate all possible locations for that num
    # - find the first group where it would fit
    # - if no groups return 0
    # - if the first group is too small then return 0
    # - else generate all fitments for that group 
    # recurse down and repeat with the cut out parts and rest of the nums

    x, ln = find_first_group_of_minimum(springs, 0)
    if x == None:
        debug("no first group")
        return 0

    springs = springs[x:] # cut off the starting dots

    first_hash = find_first_hash(springs)

    if len(nums) == 0:
        if first_hash is not None:
            return 0
        else:
            return 1

    minoff = 0
    maxoff = min(first_hash, len(springs) - num) if first_hash is not None else len(springs) - num

    debug("entry", springs, x, ln, nums, "fmm", first_hash, minoff, maxoff)

    offs = list(range(minoff, maxoff+1))
    valid_offs = []

    def valid(off):
        # check for dots inside the occupied range
        for i in range(off, off + num):
            if springs[i] == ".":
                return False

        # check that it either ends in a dot or by ending the vector
        if off+num < len(springs):
            return springs[off+num] in [".", "?"]
        else:
            return True
    offs = list(filter(valid, offs))
    debug("offs", offs, "-> valid -> ", offs, num)
    cuts = map(lambda off: off+num, offs)

    options = list(map(lambda off: springs[(num+off+1):], offs))

    debug("options", options)

    counts = list(map(lambda option: tree_count(option, nums[1:], tab+1), options))

    debug(springs, "xln", nums, x, ln)
    debug("->", options, counts, "\n")

    s = sum(counts)
    debug(s)
    return sum(counts)
###

def main():
    file = open("input12.txt", "r")
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

    # main cases
    assert tree_count(".#??#?#?.?##?#.", [6,5]) == 1

    assert tree_count("?.??#????##????#.#?", [1,1,4,3,1]) == 5 #12
    assert tree_count(".??#.???????#?.???.?", [1,7,3]) == 2 #20


#test()
main()


 

 

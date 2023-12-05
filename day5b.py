from collections import namedtuple

# 7 maps each linking into each other
# names are irrelevant

MMap = namedtuple("MMap", ["dst", "src", "num"])


# returns a list
# start without seeds
def build_maps(lines):
    lines = lines[2:]  # strip seeds and newline
    maps = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        # new section starts
        if line[-1] == ":":
            maps.append([])
            continue

        # now we're in a particular map
        [dst, src, num] = line.split(" ")
        maps[-1].append(MMap(int(dst), int(src), int(num)))

    for m in maps:
        m.sort(key=lambda e: e.src)

    return maps


def map_one(x, map):
    for e in map:
        # print("dbg", x, e)
        if x >= e.src and x < e.src + e.num:
            return x + (e.dst - e.src)
    return x


# maps a range through all mappings in a map
def map_range(a, sz, map):
    result = []

    # if it starts before anything, add it unchanged
    for mapping in map:
        if sz == 0:
            break

        if a < mapping.src:
            elems = min(mapping.src - a, sz)
            result.append((a, elems))
            # move the range
            sz -= elems
            a += elems

        if a + sz < mapping.src:
            break

        elems = min((mapping.src + mapping.num) - a, sz)
        if elems > 0:
            diff = mapping.dst - mapping.src
            result.append((a + diff, elems))
            if a + diff < 0:
                raise Exception(a, sz, diff, mapping, mapping.dst - mapping.src)
            sz -= elems
            a += elems

    if sz > 0:
        result.append((a, sz))

    return result


def seed_to_location(seed, maps):
    soil = map_one(seed, maps[0])
    fert = map_one(soil, maps[1])

    wat = map_one(fert, maps[2])
    # print("water debug", fert, "->", wat, maps[2])
    light = map_one(wat, maps[3])
    temp = map_one(light, maps[4])
    hum = map_one(temp, maps[5])
    loc = map_one(hum, maps[6])

    print(seed, ":", soil, fert, wat, light, temp, hum, loc)

    return loc


def merge_ranges(ranges):
    result = []
    result.append(ranges[0])
    for r in ranges[1:]:
        end = result[-1][0] + result[-1][1]
        if end >= r[0]:
            over = r[0] - end
            if over > 0:
                result[-1] = (result[-1][0], result[-1][1] + (r[1] - over))
        else:
            result.append(r)
    return result


def map_ranges(ranges, map):
    result = []
    for range in ranges:
        result.extend(map_range(range[0], range[1], map))
    result = sorted(result, key=lambda r: r[0])
    result = merge_ranges(result)
    return result


def new_solution(seed_pairs, maps):
    print("seedS")
    print(seed_pairs)
    print("####")
    a = map_ranges(seed_pairs, maps[0])
    print("0")
    print("####")
    print(a)
    b = map_ranges(a, maps[1])
    print("1")
    print("####")
    print(b)
    c = map_ranges(b, maps[2])
    print("2")
    print("####")
    print(c)
    d = map_ranges(c, maps[3])
    print("3")
    print("####")
    print(d)
    e = map_ranges(d, maps[4])
    print("4")
    print("####")
    print(e)
    f = map_ranges(e, maps[5])
    print("5")
    print("####")
    print(f)
    g = map_ranges(f, maps[6])
    print("6")
    print("####")
    print(g)
    return min(map(lambda r: r[0], g))


def main():
    file = open("input5.txt", "r")
    lines = file.readlines()

    seedline = lines[0].split(":")[1].strip()
    seeds = list(map(int, seedline.split()))
    seed_pairs = []
    for i in range(0, len(seeds) // 2):
        start = seeds[i * 2]
        end = seeds[i * 2 + 1]
        seed_pairs.append((start, end))

    maps = build_maps(lines)
    print(seed_pairs)

    # brute force
    expanded_seeds = []
    # for sp in seed_pairs:
    #    for i in range(sp[0], sp[0] + sp[1]):
    #        expanded_seeds.append(i)
    # locs = map(lambda seed: seed_to_location(seed, maps), expanded_seeds)
    # print(min(locs))

    # new solution
    #######
    print(new_solution(seed_pairs, maps))
    print("end")

    print("##############")

    pesky = [(18097572, 830782)]
    map_6 = [MMap(dst=329110209, src=0, num=39413233)]
    pesky_res = map_ranges(pesky, maps[6])

    print(maps[6])
    print(pesky_res)


main()

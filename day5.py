from collections import namedtuple

# 7 maps each linking into each other
# names are irrelevant

MMap = namedtuple("MMap", ["dst", "src", "num"])


# returns a list
# start without seeds
def build_maps(lines):
    maps = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        # new section starts
        if line[-1] == ":":
            if len(maps) > 0:
                maps[-1].sort(key=lambda e: e.src)
            maps.append([])
            continue

        # now we're in a particular map
        [dst, src, num] = line.split(" ")
        maps[-1].append(MMap(int(dst), int(src), int(num)))
    return maps


def map_one(x, map):
    for e in map:
        # print("dbg", x, e)
        if x >= e.src and x < e.src + e.num:
            return x + (e.dst - e.src)
    return x


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


def main():
    file = open("input5.txt", "r")
    lines = file.readlines()

    seedline = lines[0].split(":")[1].strip()
    seeds = map(int, seedline.split())
    lines = lines[2:]  # strip seeds and newline

    maps = build_maps(lines)
    locs = map(lambda seed: seed_to_location(seed, maps), seeds)

    print(locs)
    print(min(locs))


main()

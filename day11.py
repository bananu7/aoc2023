with open("input11.txt") as file:
    starmap = [line.strip() for line in file]

    galaxies = []
    ys_to_expand = set(range(0, len(starmap)))
    xs_to_expand = set(range(0, len(starmap[0])))

    for y in range(0, len(starmap)):
        for x in range(0, len(starmap[0])):
            if starmap[y][x] == '#':
                galaxies.append((x,y))
                try:
                    ys_to_expand.remove(y)
                except:
                    pass
                try:
                    xs_to_expand.remove(x)
                except:
                    pass

    SPACE_EXP = 1000000 - 1

    ## Y
    ys = iter(ys_to_expand)
    y = next(ys)
    ny = next(ys)
    count = SPACE_EXP

    galaxies_y_expanded = []

    for galaxy in sorted(galaxies, key=lambda g: g[1]):
        if galaxy[1] < y:
            galaxies_y_expanded.append(galaxy)
        else:
            if ny:
                while galaxy[1] > ny:
                    try:
                        y = ny
                        count += SPACE_EXP
                        ny = next(ys)
                    except:
                        ny = None
                        break

            galaxies_y_expanded.append((galaxy[0], galaxy[1] + count))


    ## X
    xs = iter(xs_to_expand)
    x = next(xs)
    nx = next(xs)
    count = SPACE_EXP

    galaxies_x_expanded = []

    for galaxy in sorted(galaxies_y_expanded, key=lambda g: g[0]):
        if galaxy[0] < x:
            galaxies_x_expanded.append(galaxy)
        else:
            if nx:
                while galaxy[0] > nx:
                    try:
                        x = nx
                        count += SPACE_EXP
                        nx = next(xs)
                    except:
                        nx = None
                        break

            galaxies_x_expanded.append((galaxy[0] + count, galaxy[1]))

    
    # debug print
    for y in range(0, len(starmap) + len(ys_to_expand)):
        line = ""
        for x in range(0, len(starmap[0]) + len(xs_to_expand)):
            if (x,y) in galaxies_x_expanded:
                line += "#"
            else:
                line += "."
        print(line)

    ## paths
    # sorted just to compare with example
    gs = sorted(galaxies_x_expanded, key=lambda g: g[1])
    #print(gs)

    def compute_dist(a,b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    sum = 0
    for i in range(0, len(gs)-1):
        for j in range(i+1, len(gs)):
            dist = compute_dist(gs[i], gs[j])
            #print('dist between', i+1, 'and', j+1, ' = ', dist)
            sum += dist
    print(sum)
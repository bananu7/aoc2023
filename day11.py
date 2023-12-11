with open("input11_test.txt") as file:
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

    ## Y
    ys = iter(ys_to_expand)
    y = next(ys)
    ny = next(ys)
    count = 1

    galaxies_y_expanded = []

    for galaxy in sorted(galaxies, key=lambda g: g[1]):
        if galaxy[1] < y:
            galaxies_y_expanded.append(galaxy)
        else:
            if ny:
                while galaxy[1] > ny:
                    try:
                        y = ny
                        count += 1
                        ny = next(ys)
                    except:
                        ny = None
                        break

            galaxies_y_expanded.append((galaxy[0], galaxy[1] + count))


    ## X
    xs = iter(xs_to_expand)
    x = next(xs)
    nx = next(xs)
    count = 1

    galaxies_x_expanded = []

    print(xs_to_expand)


    for galaxy in sorted(galaxies_y_expanded, key=lambda g: g[0]):
        if galaxy[0] < x:
            galaxies_x_expanded.append(galaxy)
        else:
            if nx:
                while galaxy[0] > nx:
                    try:
                        x = nx
                        count += 1
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


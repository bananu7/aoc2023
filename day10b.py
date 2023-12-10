
def find_s(maze):
    for y in range(0, len(maze)):
        for x in range(0, len(maze[y])):
            if maze[y][x] == 'S':
                return (x,y)
    raise Exception("no starting point")


NORTH = ( 0, -1)
SOUTH = ( 0, 1)
EAST = (1,  0)
WEST = (-1,  0)

def follow_path(maze, s, off):
    (sx, sy) = s
    p = s
    path = [s,p]

    while True:
        (x,y) = p

        if off == WEST:
            left = maze[y][x-1]
            p = (x-1, y)
            if left == "L":
                off = NORTH
                path.append(p)
            elif left == "F":
                off = SOUTH
                path.append(p)
            elif left == "-":
                path.append(p)
            elif left == "S":
                return path
            else:
                return None

        elif off == EAST:
            right = maze[y][x+1]
            p = (x+1, y)
            if right == "J":
                off = NORTH
                path.append(p)
            elif right == "7":
                off = SOUTH
                path.append(p)
            elif right == "-":
                path.append(p)
            elif right == "S":
                return path
            else:
                return None

        elif off == SOUTH:
            down = maze[y+1][x]
            p = (x, y+1)
            if down == "J":
                off = WEST
                path.append(p)
            elif down == "L":
                off = EAST
                path.append(p)
            elif down == "|":
                path.append(p)
            elif down == "S":
                return path
            else:
                return None

        elif off == NORTH:
            up = maze[y-1][x]
            p = (x, y-1)
            if up == "7":
                off = WEST
                path.append(p)
            elif up == "F":
                off = EAST
                path.append(p)
            elif up == "|":
                path.append(p)
            elif up == "S":
                return path
            else:
                return None

        if p == s:
            return path



with open("input10.txt") as file:
    maze = [line.strip() for line in file]

    s = find_s(maze)

    print("s", s)
    print("size", len(maze), len(maze[0]))

    # doesn't properly find S tile orientation, i did it manually
    p_n = follow_path(maze, s, NORTH)
    p_s = follow_path(maze, s, SOUTH)
    p_e = follow_path(maze, s, EAST)
    p_w = follow_path(maze, s, WEST)

    #print(p_n, p_s, p_e, p_w)
    #print(len(p_n) // 2)
    #print(len(p_s) // 2)
    #print(len(p_e) // 2)
    #print(len(p_s) // 2)

    winning_path = p_e

    counter = 0

    debug = []

    for y in range(0, len(maze)):
        inside = False

        sstart = None
        debug.append("")
        line_counter = 0

        for x in range(0, len(maze[0])):
            c = "X"
            m = maze[y][x]

            if (x,y) in winning_path:
                if m in ["L", "F", "S"]:
                    sstart = m
                elif m == "|" or m == "S" or (m == "J" and sstart in ["F"]) or (m == "7" and sstart in ["L", "S"]): # this is wrong, depends on S-tile orientation
                    if inside:
                        counter += line_counter
                        line_counter = 0
                    inside = not inside
                c = m
            elif inside:
                line_counter += 1
                c = "#"
            else:
                c = "."

            debug[-1] += c

    for dl in debug:
        print(dl)

    print()

    print(counter)

#177 - too low
# 449 - too low
# 451 - wrong, no info
# 454 - too high
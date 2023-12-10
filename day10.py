
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
    p = (s[0] + off[0], s[1] + off[1])
    path = [s,p]

    while True:
        if p == s:
            return path

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



with open("input10.txt") as file:
    maze = [line.strip() for line in file]

    s = find_s(maze)

    print("s", s)
    print("size", len(maze), len(maze[0]))

    p_n = follow_path(maze, s, NORTH)
    p_s = follow_path(maze, s, SOUTH)
    p_e = follow_path(maze, s, EAST)
    p_w = follow_path(maze, s, WEST)

    print(len(p_n) // 2)
    print(len(p_s) // 2)
    print(len(p_e) // 2)
    print(len(p_w) // 2)


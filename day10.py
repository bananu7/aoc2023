
# start 10:52

def find_s(maze):
    for y in range(0, len(maze)):
        for x in range(0, len(maze[y])):
            if maze[y][x] == 'S':
                return (x,y)
    raise Exception("no starting point")


def gen_nexts(maze, x, y):
    sx = len(maze[0])
    sy = len(maze)

    nexts = []
    if x > 0:
        if maze[y][x-1] in ["F", "-", "L", "S"]:
            nexts.append((x-1, y))
    if x < sx-1:
        if maze[y][x+1] in ["J", "-", "7", "S"]:
            nexts.append((x+1, y))
    if y > 0:
        if maze[y-1][x] in ["F", "|", "7", "S"]:
            nexts.append((x, y-1))
    if y < sy-1:
        if maze[y+1][x] in ["L", "|", "J", "S"]:
            nexts.append((x, y+1))
    return nexts


def dfs(maze, p, prev, s):
    nexts = gen_nexts(maze, p[0], p[1])
    nexts = list(filter(lambda n: n != prev, nexts))

    # blind path
    if len(nexts) == 0:
        return None

    # reached start, we have a loop
    if any(map(lambda n: n == s, nexts)):
        return [p]

    results = map(lambda n: dfs(maze, n, p, s), nexts)
    for r in results:
        if r:
            return [p] + r


with open("input10.txt") as file:
    maze = [line.strip() for line in file]

    s = find_s(maze)

    print(s)
    print(len(maze), len(maze[0]))
    #r = dfs(maze, s, s, s)
    #print(r)
    #print(len(r) // 2)

import re


def eval_path(path, nodes):
    steps = 0
    current_node_name = "AAA"
    path = path.strip()
    while True:
        for direction in path:
            if current_node_name == "ZZZ":
                return steps
            node = nodes[current_node_name]
            if direction == "L":
                current_node_name = node[0]
            else:
                current_node_name = node[1]
            steps += 1


def main():
    file = open("input8.txt", "r")
    lines = file.readlines()

    path = lines[0]

    lines = map(lambda s: s.strip(), lines[2:])

    def parse_line(line):
        match = re.search("(?P<node>.*) = \\((?P<left>.*), (?P<right>.*)\\)", line)
        if not match:
            raise Exception("WTF")
        return (match.group("node"), match.group("left"), match.group("right"))

    parsed = map(parse_line, lines)

    nodes = {}
    for node in parsed:
        nodes[node[0]] = (node[1], node[2])

    print(eval_path(path, nodes))


main()

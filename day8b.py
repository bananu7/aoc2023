import re


def all_end_in_z(names):
    return len(list(filter(lambda name: name[2] != "Z", names))) == 0


def eval_paths(path, nodes, names):
    steps = 0
    # names is a starting list
    path = path.strip()

    while True:
        for direction in path:
            if all_end_in_z(names):
                return steps

            curr_nodes = map(lambda name: nodes[name], names)

            names = []
            if direction == "L":
                for node in curr_nodes:
                    names.append(node[0])
            else:
                for node in curr_nodes:
                    names.append(node[1])
            steps += 1


def eval_path(path, nodes, start):
    steps = 0
    current_node_name = start
    path = path.strip()

    results = []
    repeats = 10

    while True:
        for direction in path:
            if current_node_name[2] == "Z":
                # return steps
                if repeats > 0:
                    results.append(steps)
                    repeats -= 1
                else:
                    return results
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
    names = []
    for node in parsed:
        nodes[node[0]] = (node[1], node[2])
        names.append(node[0])

    names = list(filter(lambda name: name.endswith("A"), names))
    print(names)

    # print(eval_paths(path, nodes, names))
    print(len(path))
    for name in names:
        print(eval_path(path, nodes, name))


main()

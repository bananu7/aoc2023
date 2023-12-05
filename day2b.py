import re

file = open("input2.txt", "r")
lines = file.readlines()

sum = 0

ids_possible = []


def compute_mins(turn):
    col_mins = [0, 0, 0]

    dice = turn.split(",")
    for d in dice:
        toks = d.split(" ")
        print(toks)
        nom = int(toks[1])
        col = toks[2]

        print(nom, col)

        if col[-1] == "\n":
            col = col[0:-1]

        if col == "red" and nom > col_mins[0]:
            col_mins[0] = nom
        if col == "green" and nom > col_mins[1]:
            col_mins[1] = nom
        if col == "blue" and nom > col_mins[2]:
            col_mins[2] = nom
    return col_mins


def accum_mins(a, b):
    return [max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])]


def power(ms):
    return ms[0] * ms[1] * ms[2]


for line in lines:
    game = line.split(":")
    id = int(game[0].split(" ")[1])

    print("########## game_id", id)

    turns = game[1].split(";")
    game_mins = [0, 0, 0]

    for turn in turns:
        print("turn")
        mins = compute_mins(turn)
        game_mins = accum_mins(game_mins, mins)

    print(power(game_mins))
    sum += power(game_mins)

print(sum)

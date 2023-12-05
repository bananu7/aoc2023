import re

file = open("input2.txt", "r")
lines = file.readlines()

sum = 0

ids_possible = []


def is_possible(turn):
    dice = turn.split(",")
    for d in dice:
        toks = d.split(" ")
        print(toks)
        nom = int(toks[1])
        col = toks[2]

        print(nom, col)

        if col[-1] == "\n":
            col = col[0:-1]

        if col == "red" and nom > 12:
            return False
        if col == "green" and nom > 13:
            return False
        if col == "blue" and nom > 14:
            return False
    return True


for line in lines:
    game = line.split(":")
    id = int(game[0].split(" ")[1])

    print("########## game_id", id)

    turns = game[1].split(";")
    possible = True
    for turn in turns:
        print("turn")
        if not is_possible(turn):
            possible = False
            break

    if possible:
        print("possible")
        sum += id
        ids_possible.append(id)

print(sum)
print(ids_possible)

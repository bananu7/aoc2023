# file = open("input4_test.txt", "r")
file = open("input4.txt", "r")
lines = file.readlines()


def tonum(s):
    return int(s.strip())


sum = 0
for line in lines:
    prs = line.split(":")
    nums = prs[1].split("|")
    win_s = nums[0].strip().replace("  ", " ").split(" ")
    mine_s = nums[1].strip().replace("  ", " ").split(" ")

    winners = list(map(tonum, win_s))
    mine = list(map(tonum, mine_s))

    # print(winners, mine)

    w_set = {}

    card_score = 0

    for w in winners:
        w_set[w] = True
    for m in mine:
        if m in w_set:
            if card_score == 0:
                card_score = 1
            else:
                card_score <<= 1

    sum += card_score

print(sum)

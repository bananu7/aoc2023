# file = open("input4_test.txt", "r")
file = open("input4.txt", "r")
lines = file.readlines()


def tonum(s):
    return int(s.strip())


card_scores = {}
for card_num, line in enumerate(lines):
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
            card_score += 1

    card_scores[card_num] = (1, card_score)

print(card_scores)

for i in range(0, len(lines)):
    (rep, sz) = card_scores[i]
    for next in range(i + 1, i + sz + 1):
        (nrep, nsz) = card_scores[next]
        card_scores[next] = (nrep + rep, nsz)

print(card_scores)

sum = 0
for i in range(0, len(lines)):
    (rep, sz) = card_scores[i]
    sum += rep

print(sum)

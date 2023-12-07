# 13 cards so let's say last two decimal digits are highest card
# pair = 100
# two pair = 200
# triple = = 300
# full = 1000
# four = 10000
# five = 100000

FIVE = 1000000
FOUR = 100000
FULL = 10000
TRIPLE = 1000
TWOPAIR = 100
PAIR = 20


def num_of_equal(hand, cardnum):
    count = 0
    for i in range(0, 5):
        if hand[i] == hand[cardnum] or hand[i] == "J":
            count += 1
    return count


def num_of_equal_old(hand, cardnum):
    count = 0
    for i in range(0, 5):
        if hand[i] == hand[cardnum]:
            count += 1
    return count


def card_value(card):
    if card.isdigit():
        return int(card)

    cards = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
    }
    return cards[card]


def sortedhand(hand):
    return "".join(sorted(hand, key=lambda card: card_value(card), reverse=True))


def five(hand):
    hand = sortedhand(hand)
    if num_of_equal(hand, 0) == 5:
        return FIVE
    else:
        return 0


def four(hand):
    hand = sortedhand(hand)
    if num_of_equal(hand, 0) == 4:
        return FOUR
    elif num_of_equal(hand, 1) == 4:
        return FOUR
    else:
        return 0


def full_house(hand):
    hand = sortedhand(hand)
    # full has just two card types padded with J
    a = None
    b = None
    for card in hand:
        if card == "J":
            continue
        if not a or a == card:
            a = card
            continue
        if not b or b == card:
            b = card
            continue
        return 0
    return FULL


def triple(hand):
    hand = sortedhand(hand)
    if num_of_equal(hand, 0) == 3:
        return TRIPLE  # + card_value(hand[0])
    elif num_of_equal(hand, 1) == 3:
        return TRIPLE  # + card_value(hand[1])
    elif num_of_equal(hand, 2) == 3:
        return TRIPLE  # + card_value(hand[2])
    else:
        return 0


def twopair(hand):
    hand = sortedhand(hand)
    groups = sorted(map(lambda i: num_of_equal(hand, i), range(0, 5)))
    # at most one joker otherwise it would be a triple
    if hand[4] == "J":
        if (
            hand[0] == hand[1]
            or hand[0] == hand[2]
            or hand[0] == hand[3]
            or hand[1] == hand[2]
            or hand[1] == hand[3]
            or hand[2] == hand[3]
        ):
            return TWOPAIR
        else:
            return 0
    else:
        groups = sorted(map(lambda i: num_of_equal_old(hand, i), range(0, 5)))
        ispair = groups == [1, 2, 2, 2, 2]
        if ispair:
            return TWOPAIR
        else:
            return 0


def pair(hand):
    hand = sortedhand(hand)
    if hand[4] == "J":
        return PAIR

    groups = sorted(map(lambda i: num_of_equal_old(hand, i), range(0, 5)))
    ispair = groups == [1, 1, 1, 2, 2]
    if ispair:
        return PAIR
    else:
        return 0


def highest_card(hand):
    return max(map(card_value, hand))


def score_hand(hand):
    if five(hand):
        return five(hand)
    elif four(hand):
        return four(hand)
    elif full_house(hand):
        return full_house(hand)
    elif triple(hand):
        return triple(hand)
    elif twopair(hand):
        return twopair(hand)
    elif pair(hand):
        return pair(hand)
    else:
        return 1  # highest_card(hand)


def ordered_hand_compare(a, b):
    for i in range(0, 5):
        if card_value(a[i]) > card_value(b[i]):
            return -1
        elif card_value(a[i]) < card_value(b[i]):
            return 1
    return 0


def hand_compare(a, b):
    s = score_hand(a)
    s2 = score_hand(b)
    if s > s2:
        return -1
    elif s < s2:
        return 1
    else:
        return ordered_hand_compare(a, b)


from functools import cmp_to_key


def bids_compare(a, b):
    (hand_a, bid_a) = a
    (hand_b, bid_b) = b
    return hand_compare(hand_a, hand_b)


# 249427326 - way too high
# 249160716 - too high
# 248750248 - correct
# 248745318 - too low
# 248573109 -


def main():
    file = open("input7.txt", "r")
    lines = file.readlines()

    hands = []
    for line in lines:
        [hand, bid] = line.strip().split(" ")

        hands.append((hand, int(bid)))

    hands.sort(key=cmp_to_key(bids_compare), reverse=True)

    sum = 0
    for rank, (hand, bid) in enumerate(hands):
        print(hand, bid)
        sum += bid * (rank + 1)
    print(sum)


main()

def cosequence(seq):
    coseq = []
    for i in range(0, len(seq) - 1):
        coseq.append(seq[i + 1] - seq[i])
    return coseq


def all_zero(seq):
    return all(map(lambda x: x == 0, seq))


def solve(seq):
    if all_zero(seq):
        return 0
    else:
        return seq[0] - solve(cosequence(seq))


def main():
    file = open("input9.txt", "r")
    lines = file.readlines()

    res_sum = 0

    for line in lines:
        line = line.strip()
        nums = list(map(int, line.split(" ")))

        result = solve(nums)
        res_sum += result
        print(result)

    print(res_sum)


main()

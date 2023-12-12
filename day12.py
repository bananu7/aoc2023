def main():
    file = open("input12_test.txt", "r")
    lines = file.readlines()

    for line in lines:
        [springs, num_str] = line.strip().split(" ")
        nums = list(map(int, num_str.split(",")))

        print(springs, nums)


main()

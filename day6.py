def compute_steps(n, t):
    steps = 0

    if n % 2 == 0:
        i = n // 2
        j = i  # n - i

        while j * i > t:
            # print(i, "*", j, "=", i * j)
            steps += 1
            i -= 1
            j += 1

        return steps
    else:
        i = n // 2
        j = n - i

        while j * i > t:
            # print(i, "*", j, "=", i * j)
            steps += 1
            i -= 1
            j += 1

        return steps


def compute_solution(n, t):
    if n % 2 == 0:
        return compute_steps(n, t) * 2 - 1
    else:
        return compute_steps(n, t) * 2


print(compute_solution(7, 9))
print(compute_solution(15, 40))
print(compute_solution(30, 200))

print()
print()
print()

# input6.txt
# Time:        42     89     91     89
# Distance:   308   1170   1291   1467

print(compute_solution(42, 308))
print(compute_solution(89, 1170))
print(compute_solution(91, 1291))
print(compute_solution(89, 1467))

print()
print()
print()

# day6b
print(compute_solution(71530, 940200))

print(compute_solution(42899189, 308117012911467))

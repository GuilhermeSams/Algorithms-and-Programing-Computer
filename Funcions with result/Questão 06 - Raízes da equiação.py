def raizes(a, b, c):
    delta = (b ** 2) - 4 * a * c
    if delta == 0:
        return 1
    elif delta < 0:
        return -1
    else:
        return 2


print(raizes(6, 11, -35))
print(raizes(2, 4, 2))
print(raizes(-4, -7, -12))

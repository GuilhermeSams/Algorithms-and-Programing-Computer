def multiplo3(n):
    for c in range(n, -1, -3):
        if n == 0:
            return True
        elif n == 1 or n == 2:
            return False


def não_multiplo3(n):
    if n == 0:
        return False
    elif n == 1 or n == 2:
        return True
    else:
        return não_multiplo3(n-3)

print(multiplo3(12))  # True
print(não_multiplo3(12))  # False
print(multiplo3(15))  # True
print(não_multiplo3(15))  # False
print(não_multiplo3(14))  # False
print(multiplo3(14))  # True

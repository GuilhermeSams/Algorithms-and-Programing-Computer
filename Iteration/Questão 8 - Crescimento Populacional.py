popA, popB = map(int, input().split(" "))
cresA, cresB = map(float, input(). split(" "))
anos = 0

while popB > popA:
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)

print(f'{anos}')
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)

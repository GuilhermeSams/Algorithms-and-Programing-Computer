string = str(input())
lendo = len(string)
cont = 0
for c in range(0, lendo // 2):
    if string[c] != string[lendo - c - 1]:
        cont += 1
if cont <= 1:
    print("ON")
else:
    print("OFF")

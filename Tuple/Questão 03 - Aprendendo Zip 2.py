lista_vaz1 = []
lista_vaz2 = []

for c in range(5):
    l1 = int(input())
    lista_vaz1.append(l1)

for i in range(5):
    l2 = int(input())
    lista_vaz2.append(l2)

ziping = zip(lista_vaz1, lista_vaz2)
var = (list(ziping))
print(var)

lista_vaz3 = []
for x in var:
    media = (sum(x) / 2)
    lista_vaz3.append(media)

print(lista_vaz3)
nome = ''
cont = -1
lista_vaz1 = []
soma = 0.0

while nome != 'Fim':
    nome, salario = map(str, input().split(","))
    lista_vaz1.append(salario)
    cont += 1
lista2 = lista_vaz1
del lista2[-1]
for c in lista2:
    c = float(c)
    soma += c


if cont != 0:
    print(f'{soma / cont:.2f}')
else:
    print('0.00')

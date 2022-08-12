nome = ''
lista_nome = []
lista_salario = []
cont = -1

while nome != "Fim":
    nome, salario = map(str, input().split(","))
    lista_nome.append(nome)
    lista_salario.append(salario)

lista_nome1 = lista_nome
del lista_nome1[-1]
print(lista_nome1)

lista_salario2 = lista_salario
del lista_salario2[-1]


for c in lista_salario2:
    c = float(c)
    print(c)
    cont += 1

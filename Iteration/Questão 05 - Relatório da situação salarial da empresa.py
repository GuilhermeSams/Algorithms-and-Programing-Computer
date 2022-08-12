qntd_entrada = int(input())
lista_nome = []
lista_salario = []
lista = []
cont = 0
cont_qntd_e = 0
soma = 0.0

if qntd_entrada == 0:
    print('Não tem média')
    print('Não tem')
    print('Não tem')
else:
    while cont_qntd_e != qntd_entrada:
        nome, salario = map(str, input().split(","))
        cont_qntd_e += 1
        lista_nome.append(nome)
        lista_salario.append(salario)
        lista.append([nome, salario])
        cont += 1

    for c in lista_salario:
        c = float(c)
        soma += c
    print(f'{soma / cont:.2f}')

lista_vaz3 = []
for x in lista_salario:
    x = float(x)
    lista_vaz3.append(x)
maxim = (max(lista_vaz3))
minin = (min(lista_vaz3))


removendo = ","

try:
    while True:
        lista.remove(removendo)
except ValueError:
    pass

print(lista)

lista_vaz5 = []
global i
for i in lista:
    i = str(i)
    lista_vaz5.append(i)
    print(lista_vaz5)
    #print(remove(lista))

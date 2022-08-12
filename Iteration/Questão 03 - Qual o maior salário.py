nome = str
global lendo_lista
lista_vaz = []
while nome != "Fim":
    nome, salario = map(str, input().split(","))
    salario = float(salario)
    lista_vaz.append(salario)
    lendo_lista = len(lista_vaz)
if lendo_lista == 1:
    print("Não tem")
else:
    del lista_vaz[-1]
    print(f'{max(lista_vaz):.2f}')

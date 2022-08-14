lista_vazia = []
qntd_entrada = int(input())
for c in range(qntd_entrada):
    nome = str(input())
    lista_vazia.append(nome)
    lista_vazia.sort(reverse=True)
for i in lista_vazia:
    print(i)

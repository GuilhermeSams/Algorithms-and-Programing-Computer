def erase(lista):
    lista_vaz = []
    for c in lista:
        lendo_tupla = len(c)

        if lendo_tupla >= 1:
            lista_vaz.append(c)
    return (lista_vaz)

lista = [(), (15,), (), (), (2, 15, 17)]
resposta = erase(lista)
print(resposta)

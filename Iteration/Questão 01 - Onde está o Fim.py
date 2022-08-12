nome = str(input())
cont = 0

while nome != 'Fim':
    nome = str(input())
    cont += 1
print(cont)


"""Você recebeu uma lista com todos os colaboradores de uma empresa. A lista contém o nome do colaborador, um por linha. 
Você não sabe o tamanho da lista, mas sabe que ela acaba quando aparece no lugar do nome a palavra "Fim".

Elabore um programa que conte a quantidade de colaboradores da empresa.


A Entrada consiste de:
um número indefinido de linhas que termina com uma linha com a palavra "Fim";
cada linha contém a string do nome do colaborador.

A Saída deve apresentar:
Um número inteiro que é a quantidade de funcionários."""
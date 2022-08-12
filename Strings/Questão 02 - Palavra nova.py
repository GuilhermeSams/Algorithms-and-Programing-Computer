palavra = str(input())
cont = 0
cont2 = 0
soma = ''
soma2 = ''
for c in palavra:
    cont += 1
    soma += c
    if cont == 2:
        break
invertida = ''.join(palavra[::-1])
for i in invertida:
    cont2 += 1
    soma2 += i
    if cont2 == 2:
        break
print(soma + ''.join(reversed(soma2)))

"""Elabore um programa que recebe uma palavra e imprime uma palavra nova derivada desta, que é composta pelos dois primeiros caracteres da palavra de entrada com os dois últimos.


A Entrada consiste de:
Uma string que contém quatro ou mais caracteres.

A Saída deve apresentar:
Uma string representando a palavra nova."""

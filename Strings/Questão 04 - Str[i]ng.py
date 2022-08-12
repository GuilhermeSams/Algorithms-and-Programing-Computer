frase = str(input())
cont = 1
cont_i = 1
soma = ''
for c in frase:
    cont += 1
    if cont % 2 != 0:
        cont_i += 1
        soma += c
for x in range(len(" ")):
    soma = soma.replace(" "[x], "")
print(soma)

qntd_amigo, valor = map(int, input().split(" "))
cont = 0
soma = 0

while cont != qntd_amigo:
    n = int(input())
    cont += 1
    soma += n

media = int(soma / qntd_amigo)
print(f'media: {media}')

if media >= valor:
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")
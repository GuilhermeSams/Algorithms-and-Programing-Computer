"""indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

if percentReclamResolPrim >= 60:
    indice = indiceReclamacao - 5
    print(f'{indice}')
else:
    indice = indiceReclamacao + 15
    print(f'{indice}')


if percentCliCancel >= 10:
    if canceladoPorProblema == 1:
        indice = indice + 80
        print(f'{indice}')
    elif canceladoPorProblema == 0:
        indice = indice + 80
        print(f'{indice}')
    else:
        indice = indice - 30
        print(f'{indice}')
else:
    if canceladoPorProblema == 1:
        indice = indice + 50
        print(f'{indice}')
    elif canceladoPorProblema == 0:
        indice = indice + 80
        print(f'{indice}')
    else:
        indice = indice - 10
        print(f'teste{indice}')


if indiceIndisponibilidade >= 10:
    indice = indice + 70
    print(f'{indice}')
else:
    indice = indice - 20
    print(f'{indice}')
"""

indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

if percentReclamResolPrim >= 60:
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

if percentCliCancel >= 10:
    if canceladoPorProblema == 1:
        indice = indice + 80

    elif canceladoPorProblema == 0:
        indice = indice - 30
else:
    if canceladoPorProblema == 1:
        indice = indice + 50

    elif canceladoPorProblema == 0:
        indice = indice - 10

print(f'{indice}')

if indiceIndisponibilidade >= 10:
    indice = indice + 70
else:
    indice = indice - 20
print(f'{indice}')

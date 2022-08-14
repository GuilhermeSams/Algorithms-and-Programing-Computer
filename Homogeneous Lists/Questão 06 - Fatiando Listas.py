lista = [int(x) for x in input().split()]

fatia1, fatia2 = map(int, input().split())

print(lista[fatia1:fatia2])
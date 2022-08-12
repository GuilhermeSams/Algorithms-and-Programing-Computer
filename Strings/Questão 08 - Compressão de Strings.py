def comprenssao(strings):
    global letra
    num = 0
    for caractere in strings:
        if caractere.isalpha():
            if num > 0:
                yield num * letra
                num = 0
            letra = caractere
        elif caractere.isdigit():
            caractere = int(caractere)
            num = (num * 10) + caractere
    yield num * letra


leitura = int(input())
for c in range(leitura):
    strings = str(input())

    print(''.join(comprenssao(strings)))

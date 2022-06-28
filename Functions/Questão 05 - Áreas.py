"""Crie uma função chamada areas que recebe 3 números inteiros (A, B e C) e calcula, em ordem:

A área de um retângulo com lados A e B;
A área de um triângulo com base B e altura C;
A área de um trapézio de altura A, base menor B e base maior C.
Apresente os valores ignorando a parte decimal.


A Entrada consiste de:
Não há dado fornecido diretamente, a função será chamada com os parâmetros definidos, que são três números inteiros, sendo C maior que B.
A Saída deve apresentar:
Três linhas apresentando os valores solicitados. Para ignorar a parte decimal, pode-se utilizar a função int().
Observação:
Apenas defina a função, o sistema se encarrega de chamá-la.

Dica:

Para ignorar a parte decimal, pode-se utilizar a função int() para mudar o tipo de ponto flutuante para inteiro.
"""


def areas(a, b, c):

    area_retangulo = a * b
    area_retangulo = int(area_retangulo)
    print(area_retangulo)

    area_triangulo = (b * c) / 2
    area_triangulo = int(area_triangulo)
    print(f'{area_triangulo:.0f}')

    area_trapesio = ((b + c) * a) / 2
    area_trapesio = int(area_trapesio)
    print(f'{area_trapesio:.0f}')


areas(1, 2, 3)


"""O caixa de um supermercado precisa dar o troco de x centavos.  Sabendo que as moedas disponíveis no caixa são de
R$ 0,50, R$ 0,25, RS 0,10, R$ 0,05 e R$ 0,01, elabore uma função chamada troco que receba o valor inteiros x, do troco
em centavos, como parâmetro e imprima a quantidade de moedas de 50, 25, 10, 5 e 1 centavos que deve dar, de forma a
minimizar a quantidade de moedas do troco.


A Entrada consiste de:
Não há dado fornecido diretamente, a função será chamada para qualquer valor arbitrário de troco definidos nos casos de
teste, que é um número inteiros x, o valor do troco em centavos.

A Saída deve apresentar:
A função troco deve imprimir a quantidade de moedas de cada valor em centavos que serão entregues como troco, sempre com
o menor número de moedas possíveis.
Por exemplo, para um troco de R$ 0,79 deve imprimir:
1 moedas de 50 centavos
1 moedas de 25 centavos
0 moedas de 10 centavos
0 moedas de 5 centavos
4 moedas de 1 centavos

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Faça um algoritmo que funcione apenas para os valores de moedas do problema, assim a função que você irá implementar
precisará usar apenas o conhecimento que você aprendeu até o presente momento na disciplina. Não use comandos e
instruções que ainda serão ensinados em lições futuras.

Descrição dos Exemplos:
Os exemplos do Moodle são autoexplicativos."""


def troco(N):
    calc_0_50 = N // 50
    N %= 50

    calc_0_25 = N // 25
    N %= 25

    calc_0_10 = N // 10
    N %= 10

    calc_0_05 = N // 5
    N %= 5

    calc_0_01 = N // 1
    N %= 1

    print(f'{int(calc_0_50)} moedas de 50 centavos')
    print(f'{int(calc_0_25)} moedas de 25 centavos')
    print(f'{int(calc_0_10)} moedas de 10 centavos')
    print(f'{int(calc_0_05)} moedas de 5 centavos')
    print(f'{int(calc_0_01)} moedas de 1 centavo')


troco(567)

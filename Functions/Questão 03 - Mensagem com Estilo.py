"""Camila gosta de ficar até tarde conversando com seus amigos. Mas, de vez em quando, Camila acaba ignorada no seu
grupo de mensagens. Ajude ela a criar mensagens que chamem mais atenção.

Crie uma função chamada estilo, que recebe um símbolo, um número e uma mensagem. O texto final deve ser a mensagem
original, rodeada pela esquerda e pela direita com o símbolo, repetido um pelo respectivo número de vezes.


A Entrada consiste de:
Não há dado fornecido diretamente, a função será chamada com parâmetros S, string com um símbolo único, N,
número inteiro e M, string com a mensagem inicial.
A Saída deve apresentar:
Uma linha com a mensagem final de Camila.
Observação:
Apenas defina a função, o sistema se encarrega de chamá-la.

Descrição dos Exemplos:
O símbolo "!" foi repetido 10 vezes, antes e depois da mensagem original."""

# S = String
# N = Quantidade que se repete
# M = Mensagem


def estilo(simbolo, qntd_simbolo, mensagem):
    print(f'{simbolo*qntd_simbolo}{mensagem}{simbolo*qntd_simbolo}')


estilo("!", 10, "Fofocas quentes")

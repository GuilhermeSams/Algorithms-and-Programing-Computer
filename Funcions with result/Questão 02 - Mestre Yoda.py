"""Frances Allen é uma grande fã do Mestre Yoda e está tentando criar um programa para inverter a ordem de algumas
sentenças. Frances quer criar um programa que receba duas sentenças e depois exiba na tela a mensagem com as sentenças
inseridas invertidas, assim como o Mestre Yoda falava na série Star Wars.


A Entrada consiste de:
Função com dois parâmetros: 1º sentença e 2º sentença;

A Saída deve apresentar:
Sentenças com a ordem invertida, separadas por vírgula.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.

Descrição dos Exemplos:
OS exemplos receberam palavras e os resultados mostrarão as palavras com a ordem invertida."""


def trocaOrdem(str1, str2):
    return str2 + "," + str1


print(trocaOrdem('Olá', 'Mundo'))
print(trocaOrdem('Você ainda tem.', 'Muito a aprender'))
print(trocaOrdem('os alunos de APC.', 'São os melhores'))

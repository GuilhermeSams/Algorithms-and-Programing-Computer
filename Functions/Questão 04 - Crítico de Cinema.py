"""Fred tem um blog sobre cinema, onde ele faz resenhas e críticas sobre os novos lançamentos das telonas. Ao final de
cada post, Fred dá uma nota de 0 a 10 para o novo filme, mas cada nota acaba ficando com uma formatação diferente. Por
isso, Fred pediu sua ajuda para criar uma formatação única para suas notas.

Crie uma função chamada nota, que recebe um valor de 0 a 10 e cria um linha formatada com essa nota da seguinte forma:

Cada linha inicia com uma barra vertical "|";
São repetidas N estrelas cheias "★", sendo N a nota do filme de 0 a 10;
São repetidos estrelas vazias "☆" até completar 10 caracteres.
A linha termina com uma barra vertical "|".

A Entrada consiste de:
Não há dado fornecido diretamente, a função será chamada com um parâmetro N, um número inteiro de 0 a 10.
A Saída deve apresentar:
Uma linha com a nota formatada.
Observação:
Apenas defina a função, o sistema se encarrega de chamá-la.

Descrição dos Exemplos:

No primeiro exemplo, a nota é zero. Portanto, existem 10 estrelas vazias entre as barras verticais.
No segundo exemplo, com nota 3, existe três estrelas cheias e 7 estrelas vazias, completando os 10 caracteres."""


def nota(num):
    estrela_cheia = f'|{num * "★"}|'
    leitura = len(estrela_cheia[1:-1])
    qntd_estrela_vazia = 10 - leitura
    estrela_cheia_sem_barra = "★" * leitura
    estrela_vazia = "☆" * qntd_estrela_vazia
    concatenamento_cheia_e_vazia = estrela_cheia_sem_barra + estrela_vazia
    print(f'|{concatenamento_cheia_e_vazia}|')


nota(3)

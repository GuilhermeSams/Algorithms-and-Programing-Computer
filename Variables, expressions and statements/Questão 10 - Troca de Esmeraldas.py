"""Menescraft é um popular jogo virtual de exploração e aventura. Nele seu objetivo é coletar recursos das mais diversas
raridades para posterior comercialização com os aldeões encontrados pelo mapa. No entanto, o sistema de trocas e vendas
deste jogo é bastante desenvolvido de modo que até mesmo os aldeões controlados pelo computador não aceitarão trocas
, onde seja cobrado um valor exorbitante. Sabendo disso, imagine que em uma jogatina você foi capaz de reunir uma
determinada quantidade de minérios de ferro, ouro, pó vermelho e diamantes. Ao pesquisar profundamente nos fóruns online
você descobriu que o valor justo de uma remessa de minérios é calculada da seguinte forma:

 Para cada minério de ferro o valor da remessa é acrescido em uma esmeralda.
 Para cada minério de ouro o valor da remessa é duplicado.
 Para cada pó vermelho o valor da remessa é acrescido em duas esmeraldas.
 Para cada diamante o valor da remessa é quadruplicado.
 É garantido que sempre haverá ao menos uma unidade de cada minério e que as quantidades encontradas de cada minério
 sempre serão números inteiros positivos. Desta forma, o valor da remessa é sempre em número de esmeraldas. Como
 apresentado, ferro e pó vermelho fornecem ao jogador o número de esmeraldas.

A Entrada consiste de:
4 inteiros F, O, P e D que representam respectivamente as quantidades de minério de ferro, ouro, pó vermelho e diamantes
encontrados.

A Saída deve apresentar:
O valor total em esmeraldas que deverá ser cobrado pela remessa de minérios, considerando o cálculo para um preço justo.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.

Descrição dos Exemplos:
No primeiro exemplo, cada minério foi encontrado exatamente uma única vez. Um minério de ferro gerou o acréscimo do
preço total em uma esmeralda, assim como um minério de pó vermelho gerou um acréscimo de duas esmeraldas, totalizando 3
esmeraldas. O valor foi então duplicado, pois havia exatamente um minério de ouro, tornando-se 6 esmeraldas e por fim
foi quadruplicado pois havia um diamante. Finalmente o preço total da remessa foi de 24 esmeraldas.
No segundo exemplo, foram encontrados 3 minérios de ferro, tornando o preço inicial 3 esmeraldas. Além disso, foram
encontrados 3 minérios de pó vermelho e como cada um equivale a duas esmeraldas, o preço total considerando apenas ferro
e pó vermelho era de 9 esmeraldas. No entanto, foram encontrados 7 minérios de ouro, o que fez com que o preço fosse
multiplicado 7*2 vezes, ou seja, 14 vezes. Além disso haviam 3 diamantes, fazendo com que o preço fosse multiplicado 3*4
vezes, ou seja, 12 vezes. Multiplicando as 9 esmeraldas iniciais por 14 e depois por 12 encontramos o valor total de
512 esmeraldas.
"""
ferro = int(input())
ouro = int(input())
po_vermelho = int(input())
diamante = int(input())
esmeralda = 0

soma_ferro_esmeralda = ferro + esmeralda
duplicado_ouro = ouro * 2
soma_povermelho_esmeralda = po_vermelho * 2
quadruplicado_diamante = diamante * 4

print(f'{((soma_ferro_esmeralda + soma_povermelho_esmeralda) * duplicado_ouro) * quadruplicado_diamante}')

"""
Susu terminou sua tarefa de matemática e para revisar mais um pouco o conteúdo ela resolveu aplicar vários números em
uma expressão numérica que ela mesma criou: para cada número x, primeiro multiplica-se x por 2, desse resultado
subtrai-se 5 e por último acrescenta-se 2x. Escreva um programa que recebe um inteiro x, o aplica na expressão de Susu
e retorna o resultado.

A Entrada consiste de:
x, um número inteiro positivo.

A Saída deve apresentar:
Um número inteiro, o resultado da expressão numérica.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.

Descrição dos Exemplos:
No primeiro exemplo, como x=7, multiplicamos o sete por dois, em seguida subtrai-se cinco desse resultado e por último
adiciona-se 27: 14−5+128=137."""

num = int(input())
print(f'{((num * 2) - 5)+(2**num)}')

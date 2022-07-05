"""
Para programar existem alguns requisitos que nossos códigos devem atender independente do problema. Para isso, algumas
perguntas podem ser feitas durante a implementação de um programa, conforme demonstra o guia abaixo. Sua tarefa é
implementar um programa que ajude os programadores a avaliarem seus códigos da mesma forma que o guia. A figura
apresenta a ordem das perguntas que deverão ser feitas.




A Entrada consiste de:
Após cada pergunta é lida uma String que pode ser do tipo 'SIM' ou 'NÃO'.

A Saída deve apresentar:
Todas as perguntas de acordo com as respostas do usuário e por fim uma das cinco possíveis respostas finais.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.

Descrição dos Exemplos:
Os exemplo são auto explicativos."""

print("O programa funciona?")
programa_funciona = str(input())
if programa_funciona == 'SIM':
    print("Você entende o que fez?")

    entende_o_que_fez = str(input())
    if entende_o_que_fez == 'SIM':
        print("Ótimo. Então não mexe!")
    else:
        print("Já foi na tutoria?")
        foi_na_tutoria_caso_dois = str(input())
        if foi_na_tutoria_caso_dois == 'SIM':
            print("Choremos!")
        else:
            print("Temos um time a disposição!")

elif programa_funciona == 'NÃO':
    print("Você sabe onde está o erro?")
    voce_sabe_onde_esta_o_erro = str(input())

    if voce_sabe_onde_esta_o_erro == 'SIM':
        print("Acha que pode solucionar sozinho?")

        solucionar_sozinho = str(input(""))

        if solucionar_sozinho == "SIM":
            print("Então mão na massa!")

        else:
            print("Já pesquisou no Google?")
            pesquisou_google = str(input())

            if pesquisou_google == 'NÃO':
                print("Corre lá então!")
            else:
                print("Já foi na tutoria?")
                foi_na_tutoria_caso_um = str(input())
                if foi_na_tutoria_caso_um == "SIM":
                    print("Choremos!")
                else:
                    print("Temos um time a disposição!")

    elif voce_sabe_onde_esta_o_erro == 'NÃO':
        print("Já foi na tutoria?")

        foi_na_tutoria = str(input())
        if foi_na_tutoria == 'SIM':
            print("Choremos!")
        else:
            print("Temos um time a disposição!")

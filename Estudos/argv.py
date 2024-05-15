#!/usr/bin/python3
#Utilizado para passagem de argumento diretamente no comando.   
import sys

#Verifica se foi passado dois argumentos.
if len(sys.argv) == 3:

    #Verifica se ambos argumentos são números.
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():

        #Pega o primeiro e segundo índice passado na linha de código e soma-se.
        valor1 = int(sys.argv[1])
        valor2 = int(sys.argv[2])
        soma = valor1 + valor2

        print("O valor ", valor1, " somado com o valor ", valor2, " é: ", soma)
    else:
        print("Digite um valor numerico")


else:
    print("Digite dois parâmetros.")
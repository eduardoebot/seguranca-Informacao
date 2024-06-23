"""
Opção 1:
arquivo = open('c:/Users/eduar/Documents/GitHub/seguranca-Informacao/Estudos/arquivo')

conteudo = arquivo.readlines()

for linha in conteudo:
    print (linha.strip())

arquivo.close()"""

#Opção 2
with open('c:/Users/eduar/Documents/GitHub/seguranca-Informacao/Estudos/arquivo') as arquivo:
    print(arquivo.readlines())
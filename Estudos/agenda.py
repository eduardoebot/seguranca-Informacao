AGENDA = {}


AGENDA["eduardo"] = {
    "telefone": "99999-8452",
    "endereco": "Rua A"
}

AGENDA["Maria"] = {
    "telefone": "99999-4452",
    "endereco": "Rua B"
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
        print("_______________________________")
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("Endereco:", AGENDA[contato]["endereco"])
        print("_______________________________")


def incluir_editar_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} editado/inserido com sucesso." .format(nome))


def editar_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} editado com sucesso." .format(nome))


def excluir_contato(nome):
     AGENDA.pop(nome)
     print("{} excluido com sucesso." .format(nome))


def menu():
     print("1 - Mostrar todos os contatos.")
     print("2 - Buscar contato específico.")
     print("3 - Incluir novo contato.")
     print("4 - Editar contato.")
     print("5 - Excluir contato.")
     print("0 - Sair do menu.")
     opcao = int(input("Digite a opção desejada."))
     
     if opcao == 1:
         mostrar_contatos()

     elif opcao == 2:
         contato = str(input("Digite o contato a ser localizado."))
         buscar_contato(contato)
    
     elif opcao == 3 or opcao == 4:
         nome = str(input("Digite o nome."))
         telefone = str(input("Digite o telefone."))
         endereco = str(input("Digite o endereco."))
         incluir_editar_contato(nome, telefone, endereco)

     elif opcao == 5:
          contato = str(input("Digite o contato a ser excluido"))
          excluir_contato(contato)

     elif opcao == 0:
          print("Menu finalizado.")

     else:
          print("Opção inválida.")

menu()
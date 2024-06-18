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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
        
    else:
        print("Agenda vazia.")


def buscar_contato(contato):
        try:
            print("_______________________________")
            print("Nome:", contato)
            print("Telefone:", AGENDA[contato]["telefone"])
            print("Endereco:", AGENDA[contato]["endereco"])
            print("_______________________________")
        
        except:
            print("Contato não cadastrado.")


def incluir_editar_contato(nome):    
    telefone = str(input("Digite o telefone."))
    endereco = str(input("Digite o endereco."))

    AGENDA[nome] = {
        "telefone": telefone,
        "endereco": endereco,
     }
    
    print("Operação realizada com sucesso.")


def editar_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} editado com sucesso." .format(nome))


def excluir_contato(nome):
    try:
        AGENDA.pop(nome)
        print("{} excluido com sucesso." .format(nome))

    except KeyError:
        print("Contato não cadastrado.")

    except:
        print("Erro inesperado.")

def menu():
    print("1 - Mostrar todos os contatos.")
    print("2 - Buscar contato específico.")
    print("3 - Incluir novo contato.")
    print("4 - Editar contato.")
    print("5 - Excluir contato.")
    print("0 - Sair do menu.")
    

while True:
    menu()
    try:
        opcao = int(input("Digite a opção desejada."))
        
    except ValueError:
        print("Opção inválida, digite um número.")
        continue

    if opcao == 1:
        mostrar_contatos()

    elif opcao == 2:
        contato = str(input("Digite o contato a ser localizado."))
        buscar_contato(contato)
    
    elif opcao == 3:
            nome = str(input("Digite o nome."))
            try:
                AGENDA[nome]
                print("Contato já cadastrado")
            except:
                print("Inserindo novo contato: {}." .format(nome))
                incluir_editar_contato(nome)

    elif opcao == 4:
            nome = str(input("Digite o nome."))
            try:
                AGENDA[nome]
                print("Editando contato: {}." .format(nome))
                incluir_editar_contato(nome)  
            except:
                print("Contato não cadastrado")


    elif opcao == 5:
        contato = str(input("Digite o contato a ser excluido"))
        excluir_contato(contato)

    elif opcao == 0:
        print("Menu finalizado.")
        break

    else:
        print("Opção inválida.")
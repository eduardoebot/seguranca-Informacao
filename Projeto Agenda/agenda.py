AGENDA = {}


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


def incluir_editar_contato(nome, telefone, endereco):    

    AGENDA[nome] = {
        "telefone": telefone,
        "endereco": endereco,
     }
    
    salvar_automaticamente()

def editar_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} editado com sucesso." .format(nome))
     salvar_automaticamente()

def excluir_contato(nome):
    try:
        AGENDA.pop(nome)
        salvar_automaticamente()
        print("{} excluido com sucesso." .format(nome))

    except KeyError:
        print("Contato não cadastrado.")

    except:
        print("Erro inesperado.")


def exportar_agenda(localArquivo):
    try:
        with open("c:/Users/eduar/Documents/GitHub/seguranca-Informacao/Estudos/"+localArquivo, "w") as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                endereco = AGENDA[contato]["endereco"]
                arquivo.write("{},{},{}\n" .format(contato, telefone, endereco))

    except Exception as error:
        print(error)
    
    
def importar_agenda(localArquivo):
    try:
        with open("c:/Users/eduar/Documents/GitHub/seguranca-Informacao/Estudos/"+localArquivo, "r") as arquivo:
            importacao = arquivo.readlines()
            for contato in importacao:
                pessoa = contato.strip().split(",")
                pessoaNome = pessoa[0]
                pessoaTelefone = pessoa[1]
                pessoaEndereco = pessoa[2]
                incluir_editar_contato(pessoaNome, pessoaTelefone, pessoaEndereco)

    except Exception as error:
        print(error)


def salvar_automaticamente():
    exportar_agenda("backup")


def menu():
    print("1 - Mostrar todos os contatos.")
    print("2 - Buscar contato específico.")
    print("3 - Incluir novo contato.")
    print("4 - Editar contato.")
    print("5 - Excluir contato.")
    print("6 - Exportar agenda.")
    print("7 - Importar agenda.")
    print("0 - Sair do menu.")
    
importar_agenda("backup")
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
                telefone = str(input("Digite o telefone."))
                endereco = str(input("Digite o endereco."))
                print("Inserindo novo contato: {}." .format(nome))
                incluir_editar_contato(nome, telefone, endereco)
                print("Operação realizada com sucesso.")

    elif opcao == 4:
            nome = str(input("Digite o nome."))
            try:
                AGENDA[nome]
                print("Editando contato: {}." .format(nome))
                telefone = str(input("Digite o telefone."))
                endereco = str(input("Digite o endereco."))
                incluir_editar_contato(nome, telefone, endereco)  
                print("Operação realizada com sucesso.")
            except:
                print("Contato não cadastrado")


    elif opcao == 5:
        contato = str(input("Digite o contato a ser excluido"))
        excluir_contato(contato)

    elif opcao == 6:
        arquivo = input("Digite o nome do arquivo para a exportação.")
        exportar_agenda(arquivo)

    elif opcao == 7:
        try:
            arquivo = input("Digite o nome do arquivo para a importação")
            importar_agenda(arquivo)
        except Exception as error:
            print("Erro ao importar ", error)

    elif opcao == 0:
        print("Menu finalizado.")
        break

    else:
        print("Opção inválida.")
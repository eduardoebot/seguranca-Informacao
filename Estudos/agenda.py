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

mostrar_contatos()
excluir_contato("eduardo")
mostrar_contatos()
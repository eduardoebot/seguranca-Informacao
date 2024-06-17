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


def incluir_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} inserido com sucesso." .format(nome))


def editar_contato(nome, telefone, endereco):
     AGENDA[nome] = {
          "telefone": telefone,
          "endereco": endereco,
     }

     print("Contato {} editado com sucesso." .format(nome))

incluir_contato("joao", "35659-4852", "Rua 65")
#mostrar_contatos()
buscar_contato("joao")
editar_contato("joao", "12345-6789", "Rua nova")
buscar_contato("joao")
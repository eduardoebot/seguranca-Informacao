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
        print("_______________________________")
        print(contato)
        print(AGENDA[contato]['telefone'])
        print(AGENDA[contato]['endereco'])
        print("_______________________________")

mostrar_contatos()
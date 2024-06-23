computadores = {
    "basico": {
        "processador": "i3",
        "memoria": "4gb",
        "armazenamento": "ssd 120gb"
    },

    "intermediario": {
        "processador": "i5",
        "memoria": "8gb",
        "armazenamento": "ssd 240gb"
    },

    "avancado": {
        "processador": "i7",
        "memoria": "16gb",
        "armazenamento": "ssd 1tb"
    }
}

for computador in computadores:
    print("A configuração do computador ", computador,":")
    print(computadores[computador]["processador"])
    print(computadores[computador]["memoria"])
    print(computadores[computador]["armazenamento"])
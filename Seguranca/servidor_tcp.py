import socket

#SOCK_STREAM: Servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #0.0.0.0: Qualquer ip pode se conectar e porta 1234.
    servidor.bind(("0.0.0.0", 1334))

    #Quantidade de conexões simultaneas (5)
    servidor.listen(5)

    #Aceitar conexão, salvar ip e cliente que conectou.
    client_socket, endereco = servidor.accept()
    print("Recebido de: " + endereco[0])

    #Receber dados até 1024 bits e transformar em string.
    while True:
        dados = client_socket.recv(1024).decode()
        print(dados)
        client_socket.send(input("Digite sua mensagem\n").encode())

    servidor.close()

except Exception as e:
    print(e)
    servidor.close()
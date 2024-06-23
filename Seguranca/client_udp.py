#Biblioteca que nos permite a fazer uma requisição. 
import socket

#AF_INET = IPV4 | #SOCK_DGRAM = UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("Digite a mensagem\n")

    #Enviar mensagem
    client.sendto(msg.encode() + "\n".encode(), ("127.0.0.1", 1234))

    #Receber resposta
    data, sender = client.recvfrom(1024)

    #Printar a resposta convertendo a variável data para string
    print(sender[0] + ": " + data.decode())
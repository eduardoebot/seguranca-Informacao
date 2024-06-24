#Biblioteca que nos permite a fazer uma requisição. 
import socket

#AF_INET = IPV4
#SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 1234))

#Com o "b" converte string para bits
client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")

#Converter bits para string e especificado para receber 1024bits.
conteudo = client.recv(1024).decode()
print(conteudo)
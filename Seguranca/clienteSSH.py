import paramiko

host = "127.0.0.1"
user = "kali"
password = "kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=password)
while True:
    stdin, stdout, stderr = client.exec_command(input("Qual comando deseja executar?"))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)
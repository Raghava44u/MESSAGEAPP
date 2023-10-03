import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen()
client,adrr=server.accept()
done=False
while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg=="quit":
        done=True
    else:
        print(msg)
    client.send(input("Type Message:").encode('utf-8'))
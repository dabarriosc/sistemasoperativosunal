import socket

port = 1194
host = "localhost"

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((host,port))

call = "hola"
cliente.send(call.encode("utf-8"))
data = cliente.recv(400)
print(data.decode("utf-8"))
cliente.close()
import socket

port = 1194
host = "localhost"

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((host,port))

while True:
        file = open(r"C:\Users\danie\Desktop\tomate_1.png", "rb")
        content = file.read(1024)
        
        while content:
            
            cliente.send(content)
            content = file.read(1024)
        
        break

try:
        cliente.send(chr(1))
except TypeError:
       
        cliente.send(bytes(chr(1), "utf-8"))
    
    
cliente.close()
file.close()
print("El archivo ha sido enviado correctamente.")
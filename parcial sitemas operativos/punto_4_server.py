from asyncio.base_events import Server
import socket

port = 1194
host = "localhost"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(64)
conn, addr = server.accept()
f = open(r"C:\Users\danie\Desktop\recibido.png", "wb")
    
while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
        except TypeError:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
    
print("El archivo se ha recibido correctamente.")
f.close()
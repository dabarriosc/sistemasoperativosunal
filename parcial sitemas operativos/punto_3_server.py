import asyncio
import socket



async def server_on_line(PORT,HOST):
     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     server.bind((HOST,PORT))
     server.listen(64)
     print("server is running")

     while True :
        connection, addr =  server.accept()
        print("CONEXION ESTABLESIDA")
        data = connection.recv(5500)
        connection.send("HTTP/1.0 200 OK\n".encode())
        connection.send("Content-type: text/html".encode())
        connection.send("\n".encode())
        connection.send(await read_HTML(r"C:\Users\danie\Desktop\parcial sitemas operativos\HTML.txt").encode("utf-8"))
        connection.close()

async def read_HTML(RUTE):

    rute_1 = RUTE
    

    archivo_1 = open(rute_1, "r")
    HTML = archivo_1.readlines()

    return HTML

asyncio.run(server_on_line(1194,"localhost"))




  
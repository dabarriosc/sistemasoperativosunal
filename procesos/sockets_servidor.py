# Daniel Barrios Caldern, Universidad Nacional de Colombia, Sistemas Operativos, 27/10/2021

import socket
import asyncio
import threading 
 
host = 'localhost'
port = 21487

servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind((host, port))

print(f"server is running{host}:{port}")

rute_1 = r"C:\Users\danie\Desktop\procesos\username.txt"
rute_2 = r"C:\Users\danie\Desktop\procesos\client.txt"

archivo_1 = open(rute_1, "r")
archivo_2 = open(rute_2, "r")

clients = []
usernames = []

print (usernames )

def send_messages(message, _client):
    for client in clients:
        if client != _client:
          client.send(message)
    
def message_controller(client):
    
  while True:  
    try:
        message = client.recv(1024)
        message_controller(message,client)
    except:
        index = clients.index(client)
        username = usernames[index]
        send_messages(f"assistant:{username} disconnect".encode())
        clients.remove(client)
        usernames.remove(username)
        client.close
        break

def autentication_connection():
    client,addres = servidor_socket.accept()
    client.send("username".encode("utf-8"))
    username = client.recv(1024).decode("utf-8") 

    message= f"assistant: {username} joined".encode("utf-8")  
    send_messages(message, client)
    client.send("connected tu server".encode("utf-8"))
    thread = threading.Thread(target=message_controller, args=(client,))
    thread.start()

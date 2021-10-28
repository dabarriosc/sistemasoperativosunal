#Daniel Barrios Calderon, Universidad Nacional de Colombia, Sistemas Operativos, 24/10/2021

import socket   
import threading

username = input("Enter your username: ")

host = 'localhost'
port = 21487

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def update_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("error")
            client.close
            break

def write_messages():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=update_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
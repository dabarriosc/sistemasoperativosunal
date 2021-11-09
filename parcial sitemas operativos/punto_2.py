import socket 
import ssl
import time
import asyncio
import os

async def socket_get_api(HOST,GET,PORT): 

    host = HOST
    port = PORT
    ssl_context = ssl.create_default_context()
    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente = ssl_context.wrap_socket(cliente, server_hostname=host)
    cliente.connect((host,port))

    get =GET.encode()
    cliente.send(get)
    data = b""
    while True:
      datos = cliente.recv(5500)
      if(len(datos)< 1):
         break
      data = data + datos 
    
    cliente.close()

    return data.decode("utf-8") 



async def write_text(FILE_NAME,get):
    
    ruta_2 = f"C:\\Users\\danie\\Desktop\\punto_2_dir\\{FILE_NAME}"
    archivo_2 = open(ruta_2, "w")
    if(get == 1):   
       get ="GET https://www.buda.com/api/v2/markets/btc-clp/ticker HTTP/1.0\r\nHost: www.buda.com \r\n\r\n"
    if(get == 2):
       get ="GET https://www.buda.com/api/v2/markets/btc-clp/order_book HTTP/1.0\r\nHost: www.buda.com \r\n\r\n"
    if(get == 3):    
       get ="GET https://www.buda.com/api/v2/markets/btc-clp/trades HTTP/1.0\r\nHost: www.buda.com \r\n\r\n"
    archivo_2.write(await socket_get_api("www.buda.com", get, 443 ))

os.mkdir(r"C:\Users\danie\Desktop\punto_2_dir")
time.sleep(3)
asyncio.run(write_text("funcion_1.txt",1))
time.sleep(3)
asyncio.run(write_text("funcion_2.txt",2))
time.sleep(3)
asyncio.run(write_text("funcion_3.txt",3))
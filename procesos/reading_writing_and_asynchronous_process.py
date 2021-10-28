#Daniel_barrios_calderon / Universidad Nacional De Colombia/ Sistemas_operativos 20/10/2021

import asyncio

async def read_txt():
    print ("hola")

    rute_1 = r"C:\Users\danie\Desktop\procesos\username.txt"


    archivo_1 = open(rute_1, "r")
    list = archivo_1.readlines()

    return list


async def write_text():

    ruta_2 = r"C:\Users\danie\Desktop\procesos\client.txt"
    archivo_2 = open(ruta_2, "w")

    duple = await read_txt()

    i = 0
    while (i < len(duple)):
    
       index = duple[i]
       archivo_2.writelines(index + "\n")
       i += 1

asyncio.run(write_text())
 
import hashlib
from os import listdir
from os.path import isdir, islink

archivo = open(r"C:\Users\danie\Desktop\parcial sitemas operativos\punto_1.py","br")
data = archivo.read()
h = hashlib.sha1()
h.update(data)

print(h.digest(), h.hexdigest())
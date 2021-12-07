import sys
import collections
file =open(r"C:\Users\danie\Desktop\resumen.txt")
output = open(r"C:\Users\danie\Desktop\map.txt","w")
list =[]
for linea in file:
    linea = linea.strip()
    palabras = linea.split()
    for palabra in palabras:
        list.append('%s\t%s' % (palabra, 1)+"\n")
new = sorted(list)
output.writelines(new)
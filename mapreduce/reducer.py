import sys

current_item = None
current_count = 0
file = open(r"C:\Users\danie\Desktop\map.txt")

for linea in file:
    linea = linea.strip()
    item, count = linea.split("\t")

    try:
        count = int(count)
    except ValueError:
        continue

    if current_item == item:
           current_count += 1
    else:
           if current_item:
                print ('%s\t%s' % (current_item, current_count))

           current_item = item
           current_count = count

if current_item == item:
   print ('%s\t%s' % (current_item, current_count))
   

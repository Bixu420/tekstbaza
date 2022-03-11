import csv
import os
import sys
sciezka=sys.argv[1]
koniec=sys.argv[2]
x=sys.argv[3]
y=sys.argv[4]
zamiana=sys.argv[5]
rows=[]
#wejscie=wejscie.split(",")
#print(wejscie)
if os.path.exists(sciezka) is False:
    print("zla sciezka")
    quit()
megalista=[]
lista=[]
lista1=[]
with open(sciezka, "r", newline="") as plik:
    reader=csv.reader(plik)
    for line in reader:
        print(line)
        megalista.append(line)

#for i in range(len(megalista)):
    #megalista[i][0].split(";")
print(megalista[0][0])
x=int(x)
y=int(y)
y1=megalista[y-1][0]
y1=y1.split(";")
print(y1[x-1])
y1[x-1]=zamiana
print(y1[x-1])
str1=";"
str2=str1.join(y1)
print(str2)
megalista[y-1][0]=str2
print(megalista)
#for y in range(len(megalista[y])):


"""for i in range(len(megalista)):
    for m in range(len(megalista[i])):
        megalista[i][m] = megalista[i][m].split(";")
for i in range(len(megalista)):
    lista1.extend(megalista[i])
for i in range(len(lista1)):
    lista.append(lista1[i])
print(lista)"""

with open(sciezka,"w", newline="") as plik:
    writer=csv.writer(plik)
    #for i in range(len(lista)):
        #for b in range(len(lista[i])):
           # writer.writerows(lista[i][b])
    writer.writerows(megalista)
os.rename(sciezka, koniec+".csv")

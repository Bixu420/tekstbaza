import csv
import os
import sys
sciezka=sys.argv[1]
koniec=sys.argv[2]
wejscie=sys.argv[3]
rows=[]
wejscie=wejscie.split(",")
print(wejscie)
megalista=[]
with open(sciezka, "r", newline="") as plik:
    reader=csv.reader(plik)
    kolumny=next(plik)
    tab=kolumny.split(";")
    for line in reader:
        megalista.append(line)
print(megalista)


with open(sciezka,"w", newline="") as plik:
    writer=csv.writer(plik)
    writer.writerow(megalista)

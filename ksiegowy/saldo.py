import sys
from main2 import Magazyn, sciezka
calkowite=0
lista=Magazyn(sciezka).lista()

for i in range(len(lista)):

    if lista[i] == "zakup":
        print(lista[i])
        lista[i + 2] = int(lista[i + 2])
        lista[i + 3] = int(lista[i + 3])
        calkowite -= (lista[i + 3] * lista[i + 2])


    if lista[i] == "sprzedarz":
        print(lista[i])
        lista[i + 2] = int(lista[i + 2])
        lista[i + 3] = int(lista[i + 3])
        calkowite += (lista[i + 3] * lista[i + 2])


    if lista[i] == "saldo":
        print(lista[i])
        lista[i + 1] = int(lista[i + 1])
        calkowite += lista[i + 1]

lista.append("saldo")
print("podaj saldo")
saldo=int(sys.argv[2])
lista.append(str(sys.argv[2]))

print("podaj komentarz")
komentarz=str(sys.argv[3])
lista.append(komentarz)


calkowite=calkowite+saldo
print(calkowite)
print(lista)
Magazyn(sciezka).zapis(lista)






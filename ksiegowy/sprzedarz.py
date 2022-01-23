import sys
from main2 import Magazyn, sciezka
r=Magazyn(sciezka)
lista=r.lista()
fundusz=r.saldo2()
magazyn=r.odczyt()
while True:
    print("podaj id produktu")
    id = input()
    lista.append(id)
    print("podaj liczbe sztuk")
    ilosc = int(input())
    lista.append(ilosc)

    print("podaj cene")
    cena=int(input())
    lista.append(cena)

    if id in magazyn:
        magazyn[id]-=ilosc
        fundusz+=cena*ilosc
    else:
        magazyn[id]=ilosc
        fundusz+=cena*ilosc
import sys
from main2 import Magazyn, sciezka

r=Magazyn(sciezka)
lista=r.lista()
fundusz=r.saldo2()
magazyn=r.odczyt()
print(fundusz)
lista.append("zakup")
for i in range(1):

    print("podaj id produktu")
    id = sys.argv[2]
    lista.append(id)
    print("podaj liczbe sztuk")
    ilosc = int(sys.argv[3])
    lista.append(ilosc)

    print("podaj cene")
    cena=int(sys.argv[4])
    lista.append(cena)

    if id in magazyn:
        magazyn[id]+=ilosc
        fundusz-=cena*ilosc
    else:
        magazyn[id]=ilosc
        fundusz-=cena*ilosc

print(magazyn)
r.zapis(lista)
print(fundusz)
import sys
from main2 import Magazyn, sciezka

r=Magazyn(sciezka)
lista=r.lista()
fundusz=r.saldo2()
magazyn=r.odczyt()
lista.append("zakup")
for i in range(1):

    id = input(sys.argv[2])
    lista.append(id)

    ilosc = int(sys.argv[3])
    lista.append(ilosc)

    cena=int(sys.argv[4])
    lista.append(cena)

    if id in magazyn:
        magazyn[id]-=ilosc
        if magazyn[id]<0:
            print("za malo produktow")
            exit()
        fundusz+=cena*ilosc
    else:
        magazyn[id]=ilosc
        fundusz-=cena*ilosc

r.zapis(lista)
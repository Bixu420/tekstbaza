import sys
logi=[]
magazyn=[]
historia=[]
komentarz=0
saldo=0
calkowite=0
arg=sys.argv[1]
calkowitailosc=0 #ilosc calkowita danego produktu
b=1
c=0
a=0
x=0
if arg=="saldo" or "zakup" or "sprzedarz":
    while (x==0):
        c=0


        logi.append(arg)
        if arg=="saldo":
            print("podaj saldo")
            saldo=int(input())
            logi.append(saldo)
            calkowite=calkowite+saldo
            print("podaj komentarz")
            komentarz=str(input())
            logi.append(komentarz)
            historia.append(["saldo", komentarz, calkowite])
        if arg=="zakup":
            print("podaj cene")
            cena=int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc=int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id=input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i]==id:
                    historia.append(["zakup", id, ilosc, cena])
                    magazyn[i+1]=magazyn[i+1]+ilosc
                    c=1

            if c!=1:
                magazyn.extend([id, ilosc])
                historia.append(["zakup", id, ilosc, cena])
            print(cena, calkowite, ilosc)
            print(magazyn)
            if cena<0 or calkowite<cena*ilosc or ilosc<0:
                print("blad")
                break
            calkowite = calkowite - cena * ilosc
        if arg=="sprzedaz":
            print("podaj cene")
            cena=int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc=int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id=input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i] == id:
                    if magazyn[i + 1] < ilosc:
                        print("nie ma tyle w magazynie")
                        a=3
                        break
                    magazyn[i + 1] = magazyn[i + 1] - ilosc
                    historia.append(["sprzedaz", id, ilosc, cena])
                    c = 1

            if c != 1:
                magazyn.extend([id, ilosc])
                historia.append(["sprzedaz", id, ilosc, cena,])
            calkowite=calkowite+cena*ilosc
            print(cena,  ilosc)
            if cena < 0  or ilosc < 0:
                print("blad")
                break
            print(magazyn, calkowite)
        if arg=="stop":
            print("wybierz: konto, magazyn, przeglad")
            polecenie=str(input())
            logi.append(polecenie)
            if polecenie=="konto":
                print(calkowite)
                break
            if polecenie=="magazyn":
                print(magazyn)
                break
            if polecenie=="przeglad":
                print("podaj zakres")
                zakres1=int(input())
                zakres2=int(input())
                print(historia[zakres1:zakres2+1])
        a=a+1
        x=x+1

    while (1 == 1):
        c = 0
        print("wybierz opcje: saldo, zakup, sprzedaz")
        I = input()
        logi.append(I)
        if I == "saldo":
            print("podaj saldo")
            saldo = int(input())
            logi.append(saldo)
            calkowite = calkowite + saldo
            print("podaj komentarz")
            komentarz = str(input())
            logi.append(komentarz)
            historia.append(["saldo", komentarz, calkowite])
        if I == "zakup":
            print("podaj cene")
            cena = int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc = int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id = input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i] == id:
                    historia.append(["zakup", id, ilosc, cena])
                    magazyn[i + 1] = magazyn[i + 1] + ilosc
                    c = 1

            if c != 1:
                magazyn.extend([id, ilosc])
                historia.append(["zakup", id, ilosc, cena])
            print(cena, calkowite, ilosc)
            print(magazyn)
            if cena < 0 or calkowite < cena * ilosc or ilosc < 0:
                print("blad")
                break
            calkowite = calkowite - cena * ilosc
        if I == "sprzedaz":
            print("podaj cene")
            cena = int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc = int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id = input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i] == id:
                    if magazyn[i + 1] < ilosc:
                        print("nie ma tyle w magazynie")
                        a = 3
                        break
                    magazyn[i + 1] = magazyn[i + 1] - ilosc
                    historia.append(["sprzedaz", id, ilosc, cena])
                    c = 1

            if c != 1:
                magazyn.extend([id, ilosc])
                historia.append(["sprzedaz", id, ilosc, cena, ])
            calkowite = calkowite + cena * ilosc
            print(cena, ilosc)
            if cena < 0 or ilosc < 0:
                print("blad")
                break
            print(magazyn, calkowite)
        if I == "stop":
            print("wybierz: konto, magazyn, przeglad")
            polecenie = str(input())
            logi.append(polecenie)
            if polecenie == "konto":
                print(calkowite)
                break
            if polecenie == "magazyn":
                print(magazyn)
                break
            if polecenie == "przeglad":
                print("podaj zakres")
                zakres1 = int(input())
                zakres2 = int(input())
                print(historia[zakres1:zakres2 + 1])
        a = a + 1
else:
    while (1 == 1):
        if arg == "konto":
            print(calkowite)
            break
        c = 0
        print("wybierz opcje: saldo, zakup, sprzedaz")
        I = input()
        logi.append(I)
        if I == "saldo":
            print("podaj saldo")
            saldo = int(input())
            logi.append(saldo)
            calkowite = calkowite + saldo
            print("podaj komentarz")
            komentarz = str(input())
            logi.append(komentarz)
            historia.append(["saldo", komentarz, calkowite])
        if I == "zakup":
            print("podaj cene")
            cena = int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc = int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id = input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i] == id:
                    historia.append(["zakup", id, ilosc, cena])
                    magazyn[i + 1] = magazyn[i + 1] + ilosc
                    c = 1

            if c != 1:
                magazyn.extend([id, ilosc])
                historia.append(["zakup", id, ilosc, cena])
            print(cena, calkowite, ilosc)
            print(magazyn)
            if cena < 0 or calkowite < cena * ilosc or ilosc < 0:
                print("blad")
                break
            calkowite = calkowite - cena * ilosc
        if I == "sprzedaz":
            print("podaj cene")
            cena = int(input())
            logi.append(cena)
            print("podaj liczbe sztuk")
            ilosc = int(input())
            logi.append(ilosc)
            print("podaj id produktu")
            id = input()
            logi.append(id)

            for i in range(len(magazyn)):
                if magazyn[i] == id:
                    if magazyn[i + 1] < ilosc:
                        print("nie ma tyle w magazynie")
                        a = 3
                        break
                    magazyn[i + 1] = magazyn[i + 1] - ilosc
                    historia.append(["sprzedaz", id, ilosc, cena])
                    c = 1

            if c != 1:
                magazyn.extend([id, ilosc])
                historia.append(["sprzedaz", id, ilosc, cena, ])
            calkowite = calkowite + cena * ilosc
            print(cena, ilosc)
            if cena < 0 or ilosc < 0:
                print("blad")
                break
            print(magazyn, calkowite)


        if arg == "konto":
            print(calkowite)
            break
        if arg == "magazyn":
            print(magazyn)
            break
        if arg == "przeglad":
            print("podaj zakres")
            zakres1 = int(input())
            zakres2 = int(input())
            print(historia[zakres1:zakres2 + 1])
        a = a + 1
print("logi:")
print(logi)
magazyn=[]
historia=[]
komentarz=0
saldo=0
calkowite=0
calkowitailosc=0 #ilosc calkowita danego produktu
b=1
c=0
a=0
while (1==1):
    c=0
    print("wybierz opcje: saldo, zakup, sprzedaz")
    I=input()
    if I=="saldo":
        print("podaj saldo")
        saldo=int(input())
        calkowite=calkowite+saldo
        print("podaj komentarz")
        komentarz=str(input())
        historia.append(["saldo", komentarz, calkowite])
    if I=="zakup":
        print("podaj cene")
        cena=int(input())
        print("podaj liczbe sztuk")
        ilosc=int(input())
        print("podaj id produktu")
        id=input()

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
    if I=="sprzedaz":
        print("podaj cene")
        cena=int(input())
        print("podaj liczbe sztuk")
        ilosc=int(input())
        print("podaj id produktu")
        id=input()

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
    if I=="stop":
        print("wybierz: konto, magazyn, przeglad")
        polecenie=str(input())
        if polecenie=="konto":
            print(calkowite)
            break
        if polecenie=="magazyn":
            print(magazyn)
            break
    a=a+1
print(historia)
paczka=20
waga=0
print("podaj ilosc paczek")
iloscpaczek=int(input())
max=iloscpaczek*paczka
suma=0
calkowitawaga=0



for i in range(1,iloscpaczek+1, 1):

    print("paczka nr", i)

    for nr in range(paczka):


        print("podaj wage")
        a = int(input())
        if a>10 or a<0:
            print("za duzy ciezar")
            continue
        waga=waga + a


        if a == 0 or waga>=20:
            print("zamykamy paczke i pakujemy kolejna")
            break
    calkowitawaga=waga+calkowitawaga
    waga = 0
print("liczba wyslanych paczek to", iloscpaczek)
print ("wyslane kilogramy=", calkowitawaga)
print ("puste kilogramy=", max-calkowitawaga)

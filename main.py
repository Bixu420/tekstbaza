print("podaj ilosc paczek")
import sys
waga=0 #ogolna waga paczki
ilosc = int(sys.argv[1])
ciezar=0 # ciezar pakunku
lacznawaga=0
nadciezar=0  #nadwaga
nrpaczki=20 #paczka z najwieksza ilosc pustych kg
samnwmco=0
i=0
while i<ilosc:
    print("podaj wage pakunku")
    ciezar=float(input())

    if ciezar==0 or waga+ciezar==20:
        if waga<nrpaczki:
            nrpaczki=i


        i=i+1

        waga=0
        print("nastepna paczka")
        continue
    if ciezar>10 or ciezar<1:
        print("podales za duza/mala waga pakunku")
        continue
    else:
        lacznawaga=lacznawaga+ciezar

    if waga + ciezar > 20:
        if waga<nrpaczki:
            nrpaczki=i
        waga=0
        nadciezar=ciezar


        i=i+1
        continue
    waga= ciezar + waga + nadciezar
    print(waga)

    print("nr paczki", i+1)

    nadciezar=0
print("liczba paczek wyslanych to", ilosc)
print("liczba kg wyslanych to", lacznawaga)
print("liczba pustych kg=", ilosc*20-lacznawaga)
print(nrpaczki+1)


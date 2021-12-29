print("podaj ilosc paczek")
ilosc=int(input())
waga=0 #ogolna waga paczki
ciezar=0 # ciezar pakunku
lacznawaga=0
nadciezar=0  #nadwaga
nrpaczki=0
for i in range (ilosc):
    print("podaj wage pakunku")
    ciezar=float(input())
    if ciezar==0 or waga==20:
        ilosc=ilosc+1
        lacznawaga=waga+lacznawaga
        waga=0
        continue
    if ciezar >10 or ciezar<1:
        print("podales za duza/mala waga pakunku")
        continue

    if waga + ciezar > 20:
        waga=0
        nadciezar=ciezar
        lacznawaga = waga + lacznawaga
        nrpaczki=nrpaczki+1
        ilosc=ilosc+1
        continue
    waga= ciezar + waga + nadciezar

    nadciezar=0
print(lacznawaga)

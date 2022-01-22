import sys
baza=[]
sciezka=sys.argv[1]

class Magazyn:
    def __init__(self, sciezka):
        self.sciezka=sciezka
        self.magazyn={}
        self.historia=[]
        self.calkowite=0

    def zakup(self,nazwa, ilosc, cena):
        saldo=ilosc*cena
        if saldo+self.calkowite<0:
            print("za mala kwota")
            return False
        if nazwa not in self.magazyn:
            self.magazyn[nazwa]=0
        self.magazyn[nazwa]+=ilosc
        self.calkowite-=saldo
        return True




    def saldo(self, saldo, komentarz):
        if saldo+self.calkowite<0:
            print("za mala kwota")
            return False
        self.calkowite+=saldo
        self.historia.append(["saldo", komentarz, calkowite])
        return True

    def odczyt(self):
        with open (self.sciezka, "r") as t:
            while True:
                linia = t.readline().strip()

                if linia == "saldo":

                    saldo = int(t.readline().strip())
                    komentarz = str(input())
                    if not self.saldo(saldo, komentarz):
                        break
        return self.magazyn

class Fundusz:
    def __init__(self, calkowite):
        self.calkowite=calkowite


    def odczyt(self ):
        with open("statussalda.txt", "r") as d:
            self.calkowite = d.read()
        self.calkowite = int(self.calkowite)
        return self.calkowite
    def wpis(self):
        self.calkowite = str(self.calkowite)
        with open("statussalda.txt", "w") as plik1:
            plik1.write(self.calkowite)
        return self.calkowite
magazyn=Magazyn(sciezka).odczyt()
print(magazyn)
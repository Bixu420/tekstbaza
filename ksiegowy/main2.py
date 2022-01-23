import sys
baza=[]
sciezka=sys.argv[1]

class Magazyn:
    def __init__(self, sciezka):
        self.sciezka=sciezka
        self.magazyn={}
        self.historia=[]
        self.calkowite=0
        self.baza=baza




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

    def lista(self):
        with open (self.sciezka, "r") as t:
            while True:
                linia = t.readline().strip()
                self.baza.append(linia)
                if linia == "":


                 break
            return self.baza

    def odczyt(self):

            lista = self.lista()
            for i in len(lista):
                if(lista[i])=="zakup":
                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]+=lista[i+2]
                        self.calkowite += lista[i + 2]
                    else:
                        self.magazyn[lista[i+1]]=lista[i+2]

                return self.magazyn
            for i in len(lista):
                if(lista[i])=="sprzedarz":
                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]-=lista[i+2]

                        return self.magazyn
                    else:
                     return False








class Fundusz:
    def __init__(self, calkowite):
        self.calkowite=calkowite



    def wpis(self):
        self.calkowite = str(self.calkowite)
        with open("statussalda.txt", "w") as plik1:
            plik1.write(self.calkowite)
        return self.calkowite
magazyn=Magazyn(sciezka).odczyt()
print(magazyn)
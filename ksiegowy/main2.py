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



    def saldo2(self):

        lista=self.lista()
        hajs=self.calkowite

        for i in range(len(lista)):

            if lista[i] == "zakup":

                lista[i + 2] = int(lista[i + 2])
                lista[i + 3] = int(lista[i + 3])
                hajs -= (lista[i + 3] * lista[i + 2])

            if lista[i] == "sprzedarz":

                lista[i + 2] = int(lista[i + 2])
                lista[i + 3] = int(lista[i + 3])
                hajs += (lista[i + 3] * lista[i + 2])

            if lista[i] == "saldo":

                lista[i + 1] = int(lista[i + 1])
                hajs += lista[i + 1]
        return hajs



    def saldo(self, saldo, komentarz):
        if saldo+self.calkowite<0:
            print("za mala kwota")
            return False
        self.calkowite+=saldo
        self.historia.append(["saldo", komentarz, calkowite])
        return True

    def lista(self):
        if self.baza:
            return self.baza
        with open (self.sciezka, "r") as t:
            for i in range(self.linie()):
                linia = t.readline().strip()
                self.baza.append(linia)




        return self.baza

    def odczyt(self):

            lista = self.lista()

            for i in range(len(lista)):
                print(lista[i])
                if lista[i]=="zakup":

                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]=self.magazyn.get(lista[i+1])+lista[i+2]
                    else:
                        self.magazyn[lista[i+1]]=lista[i+2]
                if(lista[i])=="sprzedarz":
                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]=self.magazyn.get(lista[i+1])-lista[i+2]
            return self.magazyn

    def linie(self):
        with open(self.sciezka, 'r') as fp:
            for count, line in enumerate(fp):
                pass
        return count+1
    def zapis(self, lista):
        with open(self.sciezka,"w") as plik:

            for i in range(len(lista)):
                plik.write(str(lista[i]))
                plik.write("\n")








class Fundusz:
    def __init__(self, calkowite):
        self.calkowite=calkowite



    def wpis(self):
        self.calkowite = str(self.calkowite)
        with open("statussalda.txt", "w") as plik1:
            plik1.write(self.calkowite)
        return self.calkowite

lol=(Magazyn(sciezka).saldo2())
print (lol)
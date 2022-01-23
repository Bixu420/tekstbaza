import sys
baza=[]
sciezka=sys.argv[1]

class Magazyn:
    def __init__(self, sciezka):
        self.sciezka=sciezka
        self.magazyn=[]
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
        i=0

        while i!=len(lista):
            if lista [i]=="zakup":
                self.calkowite -= int(lista[i+3])

            if lista[i]=="sprzedarz":
                self.calkowite +=int (lista[i+3])


            if lista[i]=="saldo":
                self.calkowite = int(lista[i+1])
            i=i+1
        return self.calkowite
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
            i=0
            while i!=len(lista):
                if lista[i]=="zakup":
                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]+=lista[i+2]
                        self.calkowite += lista[i + 2]
                    else:
                        self.magazyn[lista[i+1]]=lista[i+2]
                i=i+1
                return self.magazyn
            i=0
            while i!=len(lista):
                if(lista[i])=="sprzedarz":
                    lista[i+2]=int(lista[i+2])
                    if lista[i+1] in self.magazyn:
                        self.magazyn[lista[i+1]]-=lista[i+2]

                i = i + 1
                return self.magazyn


    def zapis(self, lista):
        open(self.sciezka, 'w').close()
        with open(self.sciezka, "a") as plik:

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

lol=(Magazyn(sciezka).lista())
print (len(lol))
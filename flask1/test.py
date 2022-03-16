lista=['sprzedarz', 'bib', '5', '200', 'saldo', '2000', 'lool', 'zakup', 'bleb', '1', '1000', '']
calkowite=0
b=1
class Magazyn:
    def __init__(self, lista):
        self.lista=lista
        self.b=1
        self.calkowite=0
    def odczyt(self):

        lista = self.lista()

        for i in range(len(lista)):

            if lista[i] == "zakup":
                lista[i + 2] = int(lista[i + 2])
                lista[i + 3] = int(lista[i + 3])
                self.calkowite -= (lista[i + 3] * lista[i + 2])

            if lista[i] == "sprzedarz":
                lista[i + 2] = int(lista[i + 2])
                lista[i + 3] = int(lista[i + 3])
                self.calkowite += (lista[i + 3] * lista[i + 2])

            if lista[i] == "saldo":
                lista[i + 1] = int(lista[i + 1])
                self.calkowite += lista[i + 1]
        return self.calkowite
    def bla(self):
        self.b+=2
        return self.b
i=0

def hajs(calkowite, lista):
    for i in range(len(lista)):

        if lista[i] == "zakup":
            print(lista[i])
            lista[i + 2] = int(lista[i + 2])
            lista[i + 3] = int(lista[i + 3])
            calkowite -= (lista[i + 3] * lista[i + 2])


        if lista[i] == "sprzedarz":
            print(lista[i])
            lista[i + 2] = int(lista[i + 2])
            lista[i + 3] = int(lista[i + 3])
            calkowite += (lista[i + 3] * lista[i + 2])


        if lista[i] == "saldo":
            print(lista[i])
            lista[i + 1] = int(lista[i + 1])
            calkowite += lista[i + 1]

    print(calkowite)
lista2=['saldo', '100000', 'loool', 'zakup', 'bib', '10', '100', '']






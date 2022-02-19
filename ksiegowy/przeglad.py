import sys
from main2 import Magazyn, sciezka
print("podaj zakresy")
a=int(sys.argv[2])
b=int(sys.argv[3])
lista=Magazyn(sciezka).lista()
if a or b<len(lista):
    print(lista[a+1, b+1])




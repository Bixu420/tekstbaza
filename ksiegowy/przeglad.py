import sys
from main2 import Magazyn, sciezka
print("podaj zakresy")
a=int(input())
b=int(input())
lista=Magazyn(sciezka).lista()
if a or b<len(lista):
    print(lista[a+1, b+1])




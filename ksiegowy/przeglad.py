import sys
from main2 import Magazyn, sciezka
a=int(sys.argv[2])
b=int(sys.argv[3])
lista=Magazyn(sciezka).lista()
if a or b<len(lista):
    for i in range(a-1,b-1 ):
        print(lista[i])




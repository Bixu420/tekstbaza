print("podaj kwote")
kwota =float(input())
print ("podaj oprocentowanie")

oprocentowanie = float(input())
print("podaj kwote raty")
rata = float(input())



styczen = float((1.59+oprocentowanie/1200)*kwota-rata)
print("zostalo ci "styczen)

luty =float((0.45+oprocentowanie/1200)*styczen-rata)
print("zostalo ci "luty)

marzec = float((2.32+oprocentowanie/1200)*luty-rata)
print("zostalo ci "marzec)

kwiecien = float((1.26+oprocentowanie/1200)*marzec-rata)
print("zostalo ci "kwiecien)
maj = float((1.78+oprocentowanie/1200)*kwiecien-rata)
print("zostalo ci "maj)

czerwiec = float((2.32+oprocentowanie/1200)*maj-rata)
print("zostalo ci "czerwiec)



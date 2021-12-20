print("podaj kwote")
kwota =float(input())
print ("podaj oprocentowanie")

oprocentowanie = float(input())
print("podaj kwote raty")
rata = float(input())



styczen = float((1.59+oprocentowanie/1200)*kwota-rata)
print(round(styczen,2))

luty =float((0.45+oprocentowanie/1200)*styczen-rata)
print(round(luty,2))

marzec = float((2.32+oprocentowanie/1200)*luty-rata)
print(round(marzec,2))

kwiecien = float((1.26+oprocentowanie/1200)*marzec-rata)
print(round(kwiecien,2))
maj = float((1.78+oprocentowanie/1200)*kwiecien-rata)
print(round(maj,2))

czerwiec = float((2.32+oprocentowanie/1200)*maj-rata)
print(czerwiec)
lipiec = float((1.5+oprocentowanie/1200)*czerwiec-rata)
print(round(lipiec,2))
sierpien = float((1.78+oprocentowanie/1200)*lipiec-rata)
print(round(sierpien,2))
wrzesien = float((0.7+oprocentowanie/1200)*sierpien-rata)
print(round(wrzesien,2))
pazdziernik = float((1.16+oprocentowanie/1200)*wrzesien-rata)
print(round(wrzesien,2))
listopad = float((0.4+oprocentowanie/1200)*pazdziernik-rata)
print(round(listopad,2))
grudzien = float((1.49+oprocentowanie/1200)*listopad-rata)
print(round(grudzien,2))



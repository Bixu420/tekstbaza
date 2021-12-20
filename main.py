print("podaj kwote")
kwota =float(input())
print ("podaj oprocentowanie")

oprocentowanie = float(input())
print("podaj kwote raty")
rata = float(input())



styczen = float((1+((1.59+oprocentowanie)/1200))*kwota-rata)
print(round(styczen,2))

luty =float((1+((0.45+oprocentowanie)/1200))*styczen-rata)
print(round(luty,2))

marzec = float((1+((2.32+oprocentowanie)/1200))*luty-rata)
print(round(marzec,2))

kwiecien = float((1+((1.26+oprocentowanie)/1200))*marzec-rata)
print(round(kwiecien,2))
maj = float((1+((1.78+oprocentowanie)/1200))*kwiecien-rata)
print(round(maj,2))

czerwiec = float((1+((2.32+oprocentowanie)/1200))*maj-rata)
print(round(czerwiec,2))
lipiec = float((1+((1.5+oprocentowanie)/1200))*czerwiec-rata)
print(round(lipiec,2))
sierpien = float((1+((1.78+oprocentowanie)/1200))*lipiec-rata)
print(round(sierpien,2))
wrzesien = float((1+((0.7+oprocentowanie)/1200))*sierpien-rata)
print(round(wrzesien,2))
pazdziernik = float((1+((1.16+oprocentowanie)/1200))*wrzesien-rata)
print(round(wrzesien,2))
listopad = float((1+((0.4+oprocentowanie)/1200))*pazdziernik-rata)
print(round(listopad,2))
grudzien = float((1+((1.49+oprocentowanie)/1200))*listopad-rata)
print(round(grudzien,2))

styczen1 = float((1+((1.59+oprocentowanie)/1200))*grudzien-rata)
print(round(styczen,2))

luty1 =float((1+((0.45+oprocentowanie)/1200))*styczen1-rata)
print(round(luty1,2))

marzec1 = float((1+((2.32+oprocentowanie)/1200))*luty1-rata)
print(round(marzec1,2))

kwiecien1 = float((1+((1.26+oprocentowanie)/1200))*marzec1-rata)
print(round(kwiecien1,2))
maj1 = float((1+((1.78+oprocentowanie)/1200))*kwiecien1-rata)
print(round(maj1,2))

czerwiec1 = float((1+((2.32+oprocentowanie)/1200))*maj1-rata)
print(round(czerwiec1,2))
lipiec1 = float((1+((1.5+oprocentowanie)/1200))*czerwiec1-rata)
print(round(lipiec1,2))
sierpien1 = float((1+((1.78+oprocentowanie)/1200))*lipiec1-rata)
print(round(sierpien1,2))
wrzesien1 = float((1+((0.7+oprocentowanie)/1200))*sierpien1-rata)
print(round(wrzesien1,2))
pazdziernik1 = float((1+((1.16+oprocentowanie)/1200))*wrzesien1-rata)
print(round(wrzesien1,2))
listopad1 = float((1+((0.4+oprocentowanie)/1200))*pazdziernik1-rata)
print(round(listopad1,2))
grudzien1 = float((1+((1.49+oprocentowanie)/1200))*listopad1-rata)
print(round(grudzien1,2))



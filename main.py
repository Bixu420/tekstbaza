print("podaj kwote")
kwota =float(input())
print ("podaj oprocentowanie")

oprocentowanie = float(input())
print("podaj kwote raty")
rata = float(input())



styczen = float((1+((1.59+oprocentowanie)/1200))*kwota-rata)
roznica =  kwota-styczen
print("pozostalo ci" , round(styczen,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

luty =float((1+((0.45+oprocentowanie)/1200))*styczen-rata)
roznica =  styczen-luty
print("pozostalo ci" , round(luty,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

marzec = float((1+((2.32+oprocentowanie)/1200))*luty-rata)
roznica =  luty-marzec
print("pozostalo ci" , round(marzec,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

kwiecien = float((1+((1.26+oprocentowanie)/1200))*marzec-rata)
roznica =  marzec-kwiecien
print("pozostalo ci" , round(kwiecien,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

maj = float((1+((1.78+oprocentowanie)/1200))*kwiecien-rata)
roznica =  kwiecien-maj
print("pozostalo ci" , round(maj,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

czerwiec = float((1+((2.32+oprocentowanie)/1200))*maj-rata)
roznica =  maj-czerwiec
print("pozostalo ci" , round(czerwiec,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

lipiec = float((1+((1.5+oprocentowanie)/1200))*czerwiec-rata)
print(round(lipiec,2))

sierpien = float((1+((1.78+oprocentowanie)/1200))*lipiec-rata)
roznica =  czerwiec-sierpien
print("pozostalo ci" , round(sierpien,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

wrzesien = float((1+((0.7+oprocentowanie)/1200))*sierpien-rata)
roznica =  sierpien-wrzesien
print("pozostalo ci" , round(wrzesien,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

pazdziernik = float((1+((1.16+oprocentowanie)/1200))*wrzesien-rata)
roznica =  wrzesien-pazdziernik
print("pozostalo ci" , round(pazdziernik,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

listopad = float((1+((0.4+oprocentowanie)/1200))*pazdziernik-rata)
roznica =  pazdziernik-listopad
print("pozostalo ci" , round(listopad,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

grudzien = float((1+((1.49+oprocentowanie)/1200))*listopad-rata)
roznica =  listopad-grudzien
print("pozostalo ci" , round(grudzien,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

styczen1 = float((1+((1.59+oprocentowanie)/1200))*grudzien-rata)
roznica =  grudzien-styczen1
print("pozostalo ci" , round(styczen1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

luty1 =float((1+((0.45+oprocentowanie)/1200))*styczen1-rata)
roznica =  styczen1-luty1
print("pozostalo ci" , round(luty1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

marzec1 = float((1+((2.32+oprocentowanie)/1200))*luty1-rata)
roznica =  luty1-marzec1
print("pozostalo ci" , round(marzec1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

kwiecien1 = float((1+((1.26+oprocentowanie)/1200))*marzec1-rata)
roznica =  marzec1-kwiecien1
print("pozostalo ci" , round(kwiecien1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

maj1 = float((1+((1.78+oprocentowanie)/1200))*kwiecien1-rata)
roznica =  kwiecien1-maj1
print("pozostalo ci" , round(maj1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

czerwiec1 = float((1+((2.32+oprocentowanie)/1200))*maj1-rata)
roznica =  maj1-czerwiec1
print("pozostalo ci" , round(czerwiec1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )
lipiec1 = float((1+((1.5+oprocentowanie)/1200))*czerwiec1-rata)
roznica =  czerwiec1-lipiec1
print("pozostalo ci" , round(lipiec1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )
sierpien1 = float((1+((1.78+oprocentowanie)/1200))*lipiec1-rata)
roznica =  lipiec1-sierpien1
print("pozostalo ci" , round(sierpien1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )

wrzesien1 = float((1+((0.7+oprocentowanie)/1200))*sierpien1-rata)
roznica =  sierpien1-wrzesien1
print("pozostalo ci" , round(wrzesien1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )
pazdziernik1 = float((1+((1.16+oprocentowanie)/1200))*wrzesien1-rata)

roznica =  sierpien1-wrzesien1
print("pozostalo ci" , round(wrzesien1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )
listopad1 = float((1+((0.4+oprocentowanie)/1200))*pazdziernik1-rata)
roznica =  wrzesien1-listopad1
print("pozostalo ci" , round(listopad1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )
grudzien1 = float((1+((1.49+oprocentowanie)/1200))*listopad1-rata)
roznica =  listopad1-grudzien1
print("pozostalo ci" , round(grudzien1,2), "to",round(roznica,2), "mniej niz w poprzednim miesiacu" )



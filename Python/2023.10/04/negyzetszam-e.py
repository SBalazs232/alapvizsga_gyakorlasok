#kréjünk be egy számot, momndjuk meg, hogy négyzetszám-e!

from math import sqrt

szam=int(input('Adjon meg egy számot: '))

gyok=sqrt(szam) #a szám négyzetgyöke

if gyok==round(gyok): #megegyezik-e az egészre kerekített gyökkel ( ha égész akkor igen )
    print("négyzetszám!")
else:
    print("nem négyzetszám!")
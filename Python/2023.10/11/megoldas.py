# NÉV:

# 1. Feladat
# Kérjen be a felhasználótól 2 számot (a,b)!
# A második számot úgy kérje be, amíg mindenképpen
# legyen legalább 100-zal nagyobb az első számnál. (ellenőrzés)
# Generáljon ezen az intervallumon 10 db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely 7-tel osztható.
import math
from random import randint
szam1=int(input('Szam1: '))
szam2=-math.inf # mínusz végtelen
while szam2<szam1+100:
    szam2=int(input('Szam2: '))
db=0
for i in range(10):
    generalt=randint(szam1,szam2)
    print(generalt,end=' ')
    if generalt%7==0:
        db+=1
print(f'\n{db} darab 7-tel osztható szám van.')        


#----------------------------------------------------------

#2. feladat

# Kérje be 3 felhasználó nevét és életkorát.
# Az életkort addig kérje, amíg nem megfelelő értéket kap. (18-99) (ellenőrzés)
# Határozza meg, hogy ki a legidősebb!
max_nev=''
max_ev=0
for i in range(3):
    nev=input('Név: ')
    kor=0
    while kor<18 or kor>99: 
        kor=int(input('Kor: '))
    if kor>max_ev:
        max_nev=nev
        max_ev=kor
print(f'Legidősebb: {max_nev} ({max_ev} éves)')                



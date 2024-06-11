
# 1. Feladat
# Kérjen be a felhasználótól 3 számot (a,b,n)!
# A második számot addig kérje be, amíg mindenképpen
# legyen legalább 100-zal nagyobb az 'b' az 'a'-nál. (ellenőrzés)
# Generáljon ezen az intervallumon n db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely négyzetszám.

'''
from random import randint
from math import sqrt
a=int(input("Kérem adjon meg egy számot: "))
b=int(input("Kérem adjon meg az előző számnál 100-al nagyobb számot: "))
negyzetszam=0
while a+100>b:
    b=int(input("Kérem adjon meg az előző számnál 100-al nagyobb számot: "))

n=int(input("Hány számot írjon ki a program: "))

for i in range(n):
    szam=randint(a,b)
    print(szam, end=" ")
    if sqrt(szam)==round(sqrt(szam)):
        negyzetszam+=1
print(f"\nNégyzetszámok: {negyzetszam}")
'''


#----------------------------------------------------------

#2. feladat

# Kérje be 3 felhasználó nevét és magasságát (cm), testsúlyát (kg).
# A magasság és súly adatokat addig kérje be, 
# amíg nem megfelelő értéket kap. (100-220cm/40-200 kg) (ellenőrzés)
# Határozza meg, ki a legmagasabb, és ki a legnehezebb!

legmagasabb_nev=""
legnehezebb_nev=""
max_magassag=0
max_suly=0
for i in range(3):
    nev=input("Adja meg a nevét: ")
    cm=0
    kg=0
    while cm<100 or cm>220:
        cm=int(input("Adja meg a magasságát(cm): "))
    while kg<40 or kg>200:
        kg=int(input("Adja mega a testsúlyát(kg): "))
    if cm>max_magassag:
        max_magassag=cm
        legmagasabb_nev=nev
    if kg>max_suly:
        max_suly=kg
        legnehezebb_nev=nev
print(f"A legmagasabb: {legmagasabb_nev} ({max_magassag}cm) \nA legnehezebb: {legnehezebb_nev} ({max_suly}kg)")



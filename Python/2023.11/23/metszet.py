#a metszet 2 lista közös elemit adja vissza. az eredményt beletesszük egy harmadik listában.

from random import randint

szamok1=[]
szamok2=[]

for i in range(50):
    szamok1.append(randint(-100,100))
    szamok2.append(randint(-100,100))
print(f"Számok1:\n{szamok1}")
print(f"Számok2:\n{szamok2}")

#metszet
metszet=[]

for szam in szamok1: #vegigmegyunk az 1. listan
    if szam in szamok2: #ha a szam benne van e a 2. listaban
        metszet.append(szam)
print(f"Metszete:\n{metszet}")
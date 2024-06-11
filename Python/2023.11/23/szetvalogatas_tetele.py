#szétválogatjuk a feltételnek megfelelő és a feltételnek nem megfelelő elemekre(2 külön listába)

from random import randint

szamok=[]
for i in range(50):
    szamok.append(randint(-100,100))
print(szamok)

#páros - páratlan elemek
paros_szamok=[]
paratlan_szamok=[]
for szam in szamok:
    if szam%2==0:
        paros_szamok.append(szam)
    else:
        paratlan_szamok.append(szam)
print(F'paros szamok:~n{paros_szamok}')
print(f"paratlan szamok:\n{paratlan_szamok}")
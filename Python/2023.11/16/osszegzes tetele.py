#egy lista bizonyos feltételnek megfelelő elmeit adja össze.(összeg, átlag, szorzat)
from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

#összegzés tétele

#mennyi a pozitív számok összege:

osszeg=0
for szam in szamok:
    if szam>0:
        osszeg+=szam 
print(f' a pozitív számok összege: {osszeg}')

#mennxi a paros szamok atlaga?

osszeg=0
db=0
for szam in szamok:
    if szam%2==0:
        db+=1
        osszeg+=szam
if db>0:
    print(f'A páros számok átlaga: {osszeg/db}')
else:
    print('nincs a feltételnek megfelelő elem a listában.')
    
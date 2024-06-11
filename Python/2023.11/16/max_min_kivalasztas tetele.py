#a lista legnagyobb vagy legkisebb elemét adja vissza

from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

#maximum_kivalasztas tetele:

#melyik a legnagyobb szam? (mindegy jhogy hol vagy a listában)
legnagyobb=szamok[0] #tegyuk fel hogy ez a legnagyobb ha talalunk nala nagyobbat akkor majd felul irjuk
#for szam in szamok: #ez 1* foloslegesen fog lefutni (0. elemet hasonlitja a 0. elemhez)
for i in range(1,len(szamok)):
    if szamok[1]>legnagyobb:
        legnagyobb=szamok[i]
print(f'legnagyobb elem: {legnagyobb}')

#hányadik a legnagyobb szám a listában? (ebből azt is tudjuk természetesen hogy mi a legnagyobb)
legnagyobb_indexe=0 #feltételezzük hogy az első elem
for i in range(1,len(szamok)):
    if szamok[i]>szamok[legnagyobb_indexe]:
        legnagyobb_indexe=i
print(f'A legnyagyobb szám a(z) {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe}')

#hányadik a legnagyobb páratlan szám?
#98,43,46,88,75,92,89      li=1
legnagyobb_indexe=len(szamok) #olxan indexet kell kezdőértéknek adni amit biztosan felul írunk!!
for i in range(len(szamok)):
    if szamok[i]%2==1: #ha páratlan
        if legnagyobb_indexe==len(szamok) or szamok[i]>szamok[legnagyobb_indexe]:
            legnagyobb_indexe=i
print(f'a legnagyobb páratlan szám:{szamok[legnagyobb_indexe]}')

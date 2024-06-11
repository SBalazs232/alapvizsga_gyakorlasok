#from fugvenyek import feltolt, kiir, szamok
from fugvenyek import *

feltolt(13,0,100)

#print(szamok) szebben kiirjuk a fuggvennyel
kiir()
print(f'\nElemek száma: {elemszam()}')

print(f'\nElemek összege: {osszeg()}')

print(f'Elemek átlaga: {atlag():.2f}')

bekertszam=int(input('\nKérek egy számot: '))
if keres(bekertszam):        #if keres(bekertszam)==True
    print('A keresett szám benne van a listában')
else:
    print('A keresett szám nincs benne a listában')
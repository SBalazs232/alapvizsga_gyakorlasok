from functions import *

beolvas('varosok.txt')

print(f'3.feladat: varosok szama: {len(varosok)}')
#print(f'3.feladat: varosok szama: {varosok_szama()}') ha mindent kulon fuggvenbe kell

print(f'4.feladat: indiai nagyvárosok lakosságának összege: {orszag_lakossaga("India")} fő')
print(f'4.feladat: kínai nagyvárosok lakosságának összege: {orszag_lakossaga("Kína")} fő')

legnagyobb=legnagyobb_varos()
print(f'5.feladat: a legnagyobb város:')
print(f'\tNév: {legnagyobb.nev}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')

if orszag_keres('Magyarország'):
    print('6. van mao az adatok között')
else:
    print('6. nincs mao az adatok között')

if orszag_keres('Kína'):
    print('6. van kinai az adatok között')
else:
    print('6. nincs kinai az adatok között')

print(f'7. feladat: városok egy szóközzel: {szokozos_varosook(1)} db')
print(f'7. feladat: városok kettő szóközzel: {szokozos_varosook(2)} db')
print(f'7. feladat: városok szóközök nélkül: {szokozos_varosook(0)} db')

print('8. feladat: Ország statisztika')
for key,value in orszag_statisztika().items():
    if value>6:
        print(f'\t{key} - {value} db')

print('9.feladat Kina.txt')
orszag_mentes('kina.txt','Kína')
print('9.feladat usa.txt')
orszag_mentes('usa.txt','USA')
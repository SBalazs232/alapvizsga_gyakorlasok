from dataclasses import replace
from hegyekMo import *

beolvas('hegyekMo.txt')

#print(f'3.feladat: hegycsúcsok száma: {len(hegyek)} db')
print(f'3.feladat: hegycsúcsok száma: {csucsok_szama()} db') # ha mindnet külön fuggvenybe kell irnui

print(f'4.feladat: hegycsúcsok átlagos magassága: {str(atlag_magassag()).replace(".",",")} m')

print('5.feladat a legmagasabb hegycsúcsok átlagos adatai:')
legmagasabb=legmagasabb_csucs()
print(f'\tNév: {legmagasabb.nev}')
print(f'\tHegység: {legmagasabb.hegyseg}')
print(f'\tMagasság: {legmagasabb.magassag} m')

magassag=int(input('6.feladat: kérek egy magasságot: '))
if van_magasabb(magassag)==False:
    print(f'\nNincs {magassag} m-nél magasabb hegycsúcs.')
else:
    print(f'\tvan {magassag} m-nél magasabb pl a(z) {van_magasabb(magassag)}')

print(f'7. feladat: 3000 lábnál magasabb hegycsúcsk száma: {magasabb_mint_db(3000)} ')

print('8.feladat: hegység statisztika')
for key,value in hegy_statisztika().items():
    print(f'\t{key}: {value} db')

print(f'9. feladat: mentés ')
mentes('Bükk-vidék','bukk-videk.txt')
mentes('Mátra','matra.txt')

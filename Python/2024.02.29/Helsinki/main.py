from functions import *

fajlBeolvas('helsinki.txt')

print(f'3.feladat:\nPontszerző helyezések száma: {len(eredmenyek)}')

print(f'4.feladat:\nArany: {helyezesek_szama(1)}\nEzüst: {helyezesek_szama(2)}\nBronz: {helyezesek_szama(3)}\nÖsszesen: {helyezesek_szama(1)+helyezesek_szama(2)+helyezesek_szama(3)}')

print(f'5.feladat\nOlimpiai pontok száma: {ossz_pont()}')

print(f'6.feladat:')
torna=sportag_ermek('Torna')
uszas=sportag_ermek('uszas')
if uszas>torna:
    print('Úszás sportágban szereztek több érmet')
elif uszas<torna:
    print('torna sportágban szereztek több érmet')
else:
    print('egyenlő volt az érmek száma')

fajl_bairas('helsinki2.txt')

legtobb=max_letszam()
print(f'8.feladat:')
print(f'helyezes {legtobb.helyezes}')
print(f'sportág {legtobb.sportag}')
print(f'verszenyszam {legtobb.versenyszam}')
print(f'helyezes {legtobb.helyezes}')
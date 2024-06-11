from functions import *

print('3. feladat: CB-Rádió')
beolvas('cb.txt')

#print(f'3.2 feladat: bejegyzesek szama: {len(cbadasok)} db') # ha nem kell minden fuggveny

print(f'3.2 feladat: bejegyzesek szama: {bejegyzesek_szama()} db') # ha kell minden fuggveny

print(f'3.3 feladat: sanyihoz bejegyzesek szama: {nev_bejegyzesszam("Sanyi")} db')

print(f'3.4feladat a legtobb adas:')
for adas in cbadasok:
    if adas.darab==maxadasdb():
            print(f'\tido: {adas.ora}:{adas.perc} darab {adas.darab} nev: {adas.nev}')

fajlbairas('cb2.txt')

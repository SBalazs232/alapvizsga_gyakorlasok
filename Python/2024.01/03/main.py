from nevsor import *

#hány ember van a csoportban?
print(f'A csoportba {csoport_letszam()} tanuló jár.')

#ki(k) a leghosszabb nevű tanuló(k) a csoportban?
print('leghosszabb nevű tanuló(k):')
for nev in nevek:
    if len(nev)==leghosszabb_nev_hossza():
        print(f'\t{nev}')
    
#Átlagosan milyen hosszúak a nevek az osztályban?
print(f'A csoportban a nevek átlagos hossza {atlagos_nev_hossz():.2f} karakter.')

#Van-e az osztályban keresett nevű tanuló?
keresett_nev=input('Név: ')
if nev_kereses(keresett_nev):
    print('Van iylen tanuló.')
else:
    print('nincs')
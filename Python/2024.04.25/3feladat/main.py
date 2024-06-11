from functions import *
beolvas('legmagasabb.txt')

print(f'3.2 epuletek szama {epuletek_szama()}')

print(f'3.3 emeletek osszege {emelek_osszege()}')

print(f'3.4 legmagasabb epulet adatai')
legamagasabb=legamagasabb_epulet()
print(f'\t nÉV {legamagasabb.nev}')
print(f'\t VAROS {legamagasabb.varos}')
print(f'\t osrszag {legamagasabb.orszag}')
print(f'\t megagssag {legamagasabb.magassag}')
print(f'\t elemeletk {legamagasabb.emeletek}')
print(f'\t epites eve {legamagasabb.epult}')

if orszag_keres("Olaszország"):
    print('3.5 van olasz epulet')
else:
    print('3.5 nincs olasz epulet')

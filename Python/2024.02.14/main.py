from nobel import *

beolvas('nobel.csv')

print(f'3. feladat: {tipus_nev_alapjan("Arthur B. McDonald")}')

print('4.feladat: ',end='')
if dijazott_ev_es_tipus_alapjan(217,"irodai")==False:
    print('hibás adat')
else:
    print(f'{dijazott_ev_es_tipus_alapjan(2017,"irodalmi").teljesnev}')

print("5. feladat: ")
szervezetek_adott_ev_utan(1990,'béke')

print("6. feladat: ")
dijazott_nev_tartalmazza('Curie ')

#7.feladat
print('7 feladat:')
nobeldij_statisztika()



print('8. feladat:orvosi.txt')
tipus_szerinti_faljbairas('orvosi')

print('8. feladat:fizika.txt')
tipus_szerinti_faljbairas('fizikai')
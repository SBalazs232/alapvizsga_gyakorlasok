from mukorcsolya import *

for i in range(10):
    print(f'{i+1}. versenyző pontszáma: ',end='')
    pontok=versenyzo_pontjai()
    osszpontszam=sum(pontok) #pontok lista elemeinek összege
    print(*pontok)
    print(f'\tKiesik {max(pontok)} és {min(pontok)}')
    osszpontszam-=max(pontok)-min(pontok)
    versenyzok_osszpontszama.append(osszpontszam)
    print(f'\tÁtlag pontszám: {osszpontszam/5}')

print(f'Győztes a(z) {gyoztes_versenyzo_sorszama()}. versenyző!')
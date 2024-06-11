from functions import *

print(f'A versenyen {resztvevok_szama()} versenyző indult.')

pont=8600
#pont=int(input('Adjon meg egy pont értéket: '))
print(f'{pontnal_nagyobb(pont)} versenyző ért el legalább {pont} pontot.')

print(f'A versenyzők által elért pontszámok átlaga: {pont_atalg()}')

print(f'A verseny győztese: {versenyzok[gyoztes_indexe()]} {pontok[gyoztes_indexe()]} pontos eredménnyel')

bekert_nev=input('versenyzö neve: ')
if versenyzo_pontja(bekert_nev)!=False:
    print(f'\tA versenyző pontszáma: {versenyzo_pontja(bekert_nev)}')
else:
    print('A versenyző neve nem szerepel a listában.')
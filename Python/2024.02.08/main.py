from autok import *
from os import system

betoltes('autok.txt')

while True:
    system('cls') #a képernyő törlése
    print('0-Kilépés')
    print('1-Új autó adatainak megadása')
    print('2-Adatok Listázása')
    print('3-legerőebb auto')
    print('4-adott színű autók listázása')
    valasztas=input('Választás: ')

    match valasztas:
        case '0':
            break #kilepes
        case '1':
            system('cls')
            print('új autó adatainak megadása\n')
            uj_auto_bekerese('autok.txt')
            input('Tovább...')
        case '2':
            system('cls')
            print('A nyílvántartásban lévő autók\n')
            autok_kiirasa()
            input('Tovább...')
        case '3':
            system('cls')
            print('legerősebb autó\n')
            legerosebb=legerosebb_auto()
            print(f'Rendszám: {legerosebb.rendszam}')
            print(f'Márka: {legerosebb.marka}')
            print(f'Tipus: {legerosebb.tipus}')
            print(f'Teljesítmény: {legerosebb.teljesitmeny}')
            print(f'Szín: {legerosebb.szin}')

            input('Tovább...')
        case '4':
            system('cls')
            print('Adott színű autók listázása\n')
            szin=input('Milyen színű autót keres?')
            print(f'\n{szin} színű autók: \n')
            autok_kiirasa(autok_szin_alapjan(szin))
            input('Tovább...')

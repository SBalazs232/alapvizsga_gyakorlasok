from functions import *

print('3. feladat: Toto\n3.1. feladat: Adatok beolvasása és tárolása')
beolvas('toto.txt')

print(f'3.2 feladat: Fogadási fordulók száma:{fordulokszama()}')

print(f'3.3feladat: telitalalatos szelvenyek darab szama {telitalalatosok_szama()}')

if dontetlen_e():
    print('3.4 feladat: Volt döntetlen')
else:
    print('3.4 feladat: nem Volt döntetlen')
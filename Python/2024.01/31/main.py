from tanulok import *

tanulok_feltolt(10)
tanulok_kiir()

print(f'Az osztály átlaga: {osztalyatlag():.2f}')
print(f'{atlag_folott_letszam()} tanuló van az osztályátlag fölött')
legjobb=osztaly_legjobbja()
print(f'Az osztály legjobbja: {legjobb.vezeteknev} {legjobb.keresztnev} (Átlag: {legjobb.atlag()})')
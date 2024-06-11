from functions import *

beolvas("paintings.txt")

print(f"3.3 feladat: A fájlban tárolt festmények száma: {festmenyek_szama()}")

print(f"3.4 feladat: A Pablo Picasso képek száma: {kepszam_keresese_nev_alapjan('Pablo Picasso')} darab.")

legdragabb=legdragabb_kep()
print(f'3.5 feladat: A legdrágább kép festője: {legdragabb.festo}, a kép címe: {legdragabb.festmeny}, becsült értéke: {legdragabb.becsult_ar} dollár.')

if vanE():
    print('3.6 feladat: Van olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')
else:
    print('3.6 feladat: Nincs olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')
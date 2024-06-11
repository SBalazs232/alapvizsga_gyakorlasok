from functions import *

beolvas("szavazatok.txt")
print("1.feladat")
print(f"2. feladat: a választáson {kepviselok_szama()} indult")
k_nev=input("kepviselo neve: ")
print(f'\t3.feladat: a jelölt a {kepviselo_kereses_korzetszama(k_nev)}. körzetben indult')
print(F'\t3.feladat: {kepviselo_kereses_szavazata(k_nev)}')
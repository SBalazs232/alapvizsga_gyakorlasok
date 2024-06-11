#kérjük be egy sokszög oldalainak számát
#kérkjük be egymás után az oldalak hosszát
#írjuk ki a kerületet

oldalak_szama=int(input('Kérem adja meg az oldalak számát: '))
kerulet=0

for i in range(oldalak_szama):
    oldal_hossza=int(input('adja meg az oldalak hosszát: '))
    #kerulet=kerulet+oldal_hossza
    kerulet+=oldal_hossza

print(f'Kerület: {kerulet}')
#generáljunk egy 4 jegyű PIN kódot
#kérjük meg a felhasználótól a PIN kódot
#Maximum 3x próbálkozhat. A hibás próbálkozás után írjuk ki hogy még hány esélye van.
#ha elfogyott a lehetősége akkor írjuk ki hogy: " Zárolás!"
#ha a pin kód helyett egy mesterkódot adott meg (123456), akkor mondjuk meg a pin kódot.

from random import randint

#v1:
#generálunk egy négyjegyű számot
#probléma lehet, hogy nem kezdőthet 0-val
#pint=randint(1000,9999)

#v2:
"""pin='' # a pin string tipusu
for i in range(4):
    szamjegy=randint(0,9)
    pin+=str(szamjegy) #string tipusuva kell konvertálnunk mielőtt hozzá szeretnénk fűzni 
print(pin)"""

#v3:
pin=str(randint(0,9999))
#jo_pin=pin.zfill(4) #balről vezető nullákal tölti fel megadott hosszra
jo_pin=pin.rjust(4,"0") #balről tölti fel megadott hosszal megadott karakterrel
#.ljust(4,"0") #jobbról tölti fel megadott hosszal megadott karakterrel

print(jo_pin)

mesterkod="123456"
megadott_pin=''
probalkozasok_szama=3 # max annyi lehet

while jo_pin!=megadott_pin and probalkozasok_szama>0:
    megadott_pin=input("Adja meg a PIN kódját: ")
    probalkozasok_szama-=1
    if megadott_pin==mesterkod:
        #v1:
        #print(f'Mesterkódot adott meg. Pin:{jo_pin}')
        #v2:
        print(f'Mesterkódot adott meg.')
        uj_pin=input("adja meg az új pin kódját: ")
        uj_pin2=input("adja meg az új pin kódját mégegyszer: ")
        if uj_pin==uj_pin2:
            jo_pin=uj_pin
            print('PIN kódját sikeresen megváltotatta')
            probalkozasok_szama=3



    elif jo_pin!=megadott_pin:
        print(f'Hibás PIN! Hátralévő próbálkozása száma: {probalkozasok_szama}')

if jo_pin==megadott_pin:
    print('Sikeres azonosítás!')
else:
    print("Kártyáját zároltuk!")



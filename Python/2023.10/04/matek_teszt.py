#készítsünk programot amely ki fogja kérdezni a matekot
#2 szám különbsége/összege/szorzata
#a prgram akkor ér véget ha a felhasználó 5 feladatot jól csinál
#rossz válasz esetén újrakérdezizuk ugyanazt a példát
#a végén kiírjuk az eredményességet %-ban

from random import randint

kerdesek_szama=5 # cak itt kell átírna ha változtatni szeretnénk

rossz_valasz_szama=0

for i in range(kerdesek_szama):
    szam1=randint(1,10)
    szam2=randint(1,10)
    muvelet=randint(0,2) # 0='+' 1= '-' 2='*'
    helyes_valasz=False  #kezdőérték a while ciklushoz
    while helyes_valasz==False:
        match muvelet:
            case 0: # +
                valasz=int(input(f'{szam1}+{szam2}='))
                if  valasz==szam1+szam2:
                    print('Jó válasz')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valasz_szama+=1
            case 1: # -
                valasz=int(input(f'{szam1}-{szam2}='))
                if  valasz==szam1-szam2:
                    print('Jó válasz')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valasz_szama+=1
            case 2: # *
                valasz=int(input(f'{szam1}*{szam2}='))
                if  valasz==szam1*szam2:
                    print('Jó válasz')
                    helyes_valasz=True
                else:
                    print('Rossz válasz!')
                    rossz_valasz_szama+=1
print(f"Eredményesség: {kerdesek_szama/(kerdesek_szama+rossz_valasz_szama)*100:.2f}")

#KÉSŐBB: fgv használata mert itt kb ugyanazt csináltuk háromszor
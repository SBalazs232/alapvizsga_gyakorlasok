#3sszor dobunk egy sima dobókokával, összeadjuk az értékeket ha za összeg kisbb mmint 10 akkor Anni nyert különben  Panni
#kérkük be hány feldobás legyen majd mondjuk meg ki hányszor nyert
from random import randint
anni_nyert=0

feldobasok_szama=int(input("Hány dobás legyen: "))

for i in range(feldobasok_szama):
    dobas1=randint(1,6)
    dobas2=randint(1,6)
    dobas3=randint(1,6)
    osszeg=dobas1+dobas2+dobas3
    if osszeg<10:
        print('Anni nyert!')
        anni_nyert+=1
    else:
        print("Panni nyert!")
print(f'A játék során {anni_nyert} alkalommal Anni, {feldobasok_szama-anni_nyert} alkalommal Panni nyert.')
#generáljunk egy 1 és 100 közé eső számot 
# a játékos feladata: hogy ezt kitalálja
#segítség: a tipp kissebb-e vagy nagyobb mint a keresett szám

from random import randint
titkos_szam=randint(1,100)
#print(titkos_szam) # csak a tesztelés miatt

tipp=-1  #a játékos tippje
tippek_szama=0 #kezdetben 0 , utána tippenként növeljük

while tipp != titkos_szam: #addig megy, amíg el nem találjuk
    tipp_txt=input('Tipp (1,100): ')
    tippek_szama+=1
    if tipp_txt.isnumeric(): #csak akkor viszgaljuk ha pozitiv egesz szam
        tipp=int(tipp_txt)
        if tipp>titkos_szam: #ha a tippunk nagy
            print('Kisebb!')
        elif tipp<titkos_szam: #ha a tippunk tul kicsi
                print('Nagyobb!')
print(f'Teli Találat!, {tippek_szama} tippre volt szükség')
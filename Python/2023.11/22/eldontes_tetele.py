#döntsük el hogy valamilyen fletételnek megfelelő elem a listában
#válasz: IGEN vagy NEM 
#A keresést ne folytassa ha a választ meg tudja adni!

#van e 13mal osztható szam a listában?

szamok=[11,26,33,12,3]
print(szamok)

#v1:
#hivatalos algoritmus (minden programozási nyelven megvalósítható)
index=0
while index<len(szamok) and szamok[index]%13!=0:
    index+=1
if index==len(szamok):
    print('Nincs 13mal osztható szám a listában')
else:
    print('Van 13mal osztható szám a listában')

#v2:
#python specifikus megoldás
for szam in szamok:
    if szam%13==0:
        print("Van 13mal osztható szám a listában")
        break #az első teljesüléskor kiugrika ciklusból
else: #csak akkor lép bele ha a forban nem volt break
    print('Nincs 13mal osztható szám a listában')

#v3:
#később saját függvénnyel:
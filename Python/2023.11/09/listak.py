#Eddig pl 4 adathoz 4 változo kellett
#a=1
#b=272
#c=112
#d=12323

#lista közös név alatt, sorszámmal indexelve tárol elemeket
lista=[] #üres lista

szamok=[111,34,66,78,5,15,30000,6312,1283,78462,167]
szinek=['zöld',"kék","piros","barna"]

#lista elemeinek elérése
print(szamok) #teljes lista kiirasa (pl teszteles)
print(*szinek,sep=', ') #lista összes elmének kiírása

#a lista elemszáma
print(len(szamok))


#a lista elemeit 0tol kezdve indexeljuk
#az elso elem indexe a 0, az utolsó elem indexe n-1
print(szamok[0]) #a lista elso eleme
print(szamok[-1]) # a lista utolso eleme
print('utolso elem v2:',szamok[len(szamok)-1])

#a lista végigjárása, ha az index is kell:
for i in range(len(szinek)):
    print(f'{i+1}. {szinek[i]}')
    #egymás alá írjuk a színek lista elemeit szorszamozva


#a lista végigjárása ha az index nem kell
for szin in szinek:
    print(szin,end=" ")

#3-mal oszthato elemk zsáma  a szamok listavban:
db=0
for szam in szamok:
    if szam%3==0:
        db+=1
print(f"\n{db} db 3-mal osztható szám van a szamok listában.")

#lista feltöltése random elemekkel
from random import randint

ujszamok=[]
for i in range(100): #100 elemű listához
    ujszamok.append(randint(-100,100))
    #append metódus elem hozzáadása a listához
print(*ujszamok)
#részlista kiírása:
#listaneve[ol:ig]   tol-incluasive, ig-exclusive
print(ujszamok[1:4]) #1-4-ig részlista, de a 4-es indexu már nincs benne
print(ujszamok[3:]) #3m. indexutől a végéig
print(ujszamok[:4])# a lista elejétől a 4.ig de a 4es indexű már nics benne
print(ujszamok[-3:])#utolsó 3 elem

from fileinput import close


fajl=open('gyumolcsok.txt','r',encoding='UTF8')
#'gyumolcsok.txt' -fájl amit beolvasunk
#r - megnyitás módja read olvasás
#encoding UTF8 karakterkódolás

egysor=fajl.readline() #beolvas egy sort a fájlból és a mutatót a következő sorra állítja
egysor=egysor.strip() #levágja a sor elejéről és végéről a láthatatlan elemeketpl soremeles

kovetkezosor=fajl.readline().strip() #egy utasitasban nem kulon
fajl.close() #fájl bezárása !!!FONTOS!!!FŐLEG!!!ÍRÁSNÁL!!!
print(egysor)
print('szalma barma barna')
print(kovetkezosor)
print('------------------')

#teljes fájl beolvasása
gyumolcsok=[]
fajl=open('gyumolcsok.txt','r',encoding='UTF-8')

for sor in fajl: #végig megy a fájl sorain
    gyumolcsok.append(sor.strip())

fajl.close()
print(gyumolcsok)
print('------------------')
gyumolcsok.clear() #kiuritjuk a listat hogy akovetkezo feladatban is használni tudjuk
#ha fejléc is van
fajl=open('gyumolcsok_fejleccel.txt','r',encoding='UTF-8')
fajl.readline() #átugorjuk
#fejlec=fajl.readline() #ha később még kellene

for sor in fajl: #végig megy a fájl sorain
    gyumolcsok.append(sor.strip())

fajl.close()
print(gyumolcsok)

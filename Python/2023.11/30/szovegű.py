mondat='Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia praesentium beatae doloremque magni quidem corporis nobis deleniti, sed facere numquam quis officiis tempora. Ratione, rerum mollitia! Aliquid nesciunt deserunt quasi.'

# milyen hosszú a mondat?
print(f"A mondat {len(mondat)} karakterből áll.")
print(f"A mondat {len(mondat.replace(' ',''))} karakterből áll szóközök nélkül.")


#hány szóból áll a mondat? (szóközok szama+1)
#v1
db=0
for betu in mondat:
    if betu==' ':
        db+=1
print(f'a Mondat {db+1} szóból áll')
#v2
szavak=mondat.split(' ')#határolókarakter (szóköz) mentén szétdaraboljuk a mondatot és a szavak listába tesszük
print(f'A mondat {len(szavak)} szóbol áll')

#hány olyan szó van a szövegben ami legalább 10 karakter hosszú
irasjelek='([{,.?!-_:}])/%' #nem kivanatos karakterek torlese
for irasjel in irasjelek:
    mondat2=mondat.replace(irasjel,'')

szavak2=mondat2.split(' ')
db=0
for szo in szavak2:
    if len(szo)>=10:
        db+=1
print(f'A szövegben {db} db szó van amely legalább 10 karakter hossz')

#kérjünk be egy karaktert es mondjuk meg hogy mennyi vn belole
bekert_karakter=input('karaker: ')
db=0
for betu in  mondat:
    if betu==bekert_karakter:
        db+=1
print(f"Aa szovegben ennyi {bekert_karakter} betu van {db}")

#melyik karaktelrbol mennyinf ayjfbnfjha a modnadtagab ahf
lehetseges_karakterek='qwertzuiopőúasdfghjkléáűíyxcvbnmöüó'

karakterek_szama=[]
for lehetseges_karakter in lehetseges_karakterek:
    db=0
    for karakter in mondat:
        if karakter.upper()==lehetseges_karakter.upper():
            db+=1
    karakterek_szama.append(db)

print('karakter statisztika:')
for i in range(len(lehetseges_karakterek)):
    if karakterek_szama[i]>0:
        print(f'{lehetseges_karakterek[i]}:{karakterek_szama[i]}')

#melyik karakterbol van a legtöbb szövegböl
max_index=0
for i in range(1,len(karakterek_szama)):
    if karakterek_szama[i]>karakterek_szama[max_index]:
        max_index=i
print(f'A {lehetseges_karakterek[max_index]} karakterekből van legtöbb ({karakterek_szama[max_index]} db)')
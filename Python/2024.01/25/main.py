from versenyzo import versenyzo

versenyzok:list[versenyzo]=[]

versenyzok.append(versenyzo("Eril",7.56,8.12,6.45))
versenyzok.append(versenyzo("Pop Simon",6.66,7.12,6.98))
versenyzok.append(versenyzo("Amper",8.01,8.87,7.32))
versenyzok.append(versenyzo("Trab Antal",6.87,5.65,6.74))

print('-------------------------------------------------')
print('|     Név       |  1.  |  2.  |  3.  |Legnagyobb|')
print('-------------------------------------------------')

for v in versenyzok:
    print(f'|{v.nev.ljust(15)}| {v.elso} | {v.masodik} | {v.harmadik} | {str(v.legnagyobb_ugras()).rjust(6)}   |')
    print('-------------------------------------------------')

    #hány olyan versenyző van, akinek mindhárom ugrása 6.5 m feletti?

mind_hatesfel_feletti=0 #versenyzők szama
for v in versenyzok:
    if v.elso>6.5 and v.masodik>6.5 and v.harmadik>6.5:
        mind_hatesfel_feletti+=1
print(f'\n{mind_hatesfel_feletti} versenyzőnek nagyobb mindhárom ugrása, mint 6.5 méter.')

#ki nyerte a versenyt és mekkora ugrásaal?
gyoztes_indexe=0
for i in range(1,len(versenyzok)):
    if versenyzok[i].legnagyobb_ugras()>versenyzok[gyoztes_indexe].legnagyobb_ugras():
        gyoztes_indexe=i
print(f'Győztes: {versenyzok[gyoztes_indexe].nev} ({versenyzok[gyoztes_indexe].legnagyobb_ugras()})')

#Keresett versenyző legnagyobb ugrása meghatározása.
bekert_nev=input('\nkeresett versenyzo: ')
for v in versenyzok:
    if v.nev.upper()==bekert_nev.upper():
        print(f'{v.nev} legnagyobb ugrása: {v.legnagyobb_ugras()} méter.')
        break
else:
    print('Nincs ilyen versenyző!')

szotar={'alma':'apple','szék':'chair','ajtó':'door','kék':'blue'}
        #key:value

print(szotar)
print(szotar['kék']) #ki irja a valeu tartalmát

for szo in szotar.keys(): #végigmegyunk a szotar key mezoin
    print(szo)            #és kiirjuk azokat

for szo in szotar.items():  #egesz szotar
    print(szo)

szotar['piros']='red'  #dict_neve['key_mező']=value_mező

#meglevő elem flül irasa
szotar['kék']='navy'

for key,value in szotar.items():  #egesz szotar
    print(f'{key} - {value}')


#HIBA ha olyan kulcsa hivatkozunk ami nincs a szótárban
#print(szotar['barna']) #KeyError

#kereses szótárban key mező alapján
keresett_szo=input('szo: ')
if keresett_szo in szotar.keys(): #ha megtalaltuk
    print(f'{keresett_szo}-{szotar[keresett_szo]}')
else:
    print('Nincs ilyen szó!')
    if input('Szeretné felvenni? (i/n): ')=='i':
        jelentes=input('jelentése: ')
        szotar[keresett_szo]=jelentes

print(szotar)
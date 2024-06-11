import random #véletlen szám generáláshoz szükséges

for i in range(20): #20 db szám 20szor fut le
    print(random.randint(1,10), end=" ") #generál 1db 1-10 közötti( határokkal) egesz szamot majd kiírjuk

x=random.random()  #valos szam DE 0<=X<1
print(f'\n{x}')

y=random.randrange(0,101,2) #random páros szám 0-100 között (felső határ nincs bent mint a range-nél)
print(f'\n{y}')
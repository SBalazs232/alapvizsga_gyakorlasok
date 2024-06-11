#0 1 1 2 3 5 8 13 21
#0. eleme a 0
#1. eleme az 1
#további elemeket az előző 2 elem összege határozza meg
#aktuáli_elem=előző+előző előtti

#kérjük be a felhasznalatol, hogy hány elemű legyen a sorozat (n), és írjuk ki az első n elemet

n=int(input('Hány elemű legyen a sorozat?: '))

elozo_elotti=0
elozo=1

if n>=2:
    print('0 1 ',end='')
elif n==1:
    print('0')

for i in range(n-2): # pl a 10 elemu sorozatnal (mivel az első 2 elem mar megvan) 8 elem kell
    aktualis=elozo_elotti+elozo
    print(aktualis, end=' ')
    elozo_elotti=elozo
    elozo=aktualis
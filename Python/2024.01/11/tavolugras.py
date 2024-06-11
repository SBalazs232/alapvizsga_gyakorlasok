#12 versenyzo
#mindenki 6ot ugrik
#ugrások 7-8.5 között legyenek
#30% esély, hogy érvénytelen
#szimuláljuk le a versenyt!!!!!!!!

#1. versenyző ugrásai : 7.8 8.1 érvénytelen 7.56 8.11 ervenytelenú
#1.versenyzo legnagyobb ugrasa: 8.11

from random import randint

def ugrasok_generalasa()->list[float]:
    ugrasok=[]
    for i in range(6):
        egy_ugras= randint(700,850)/100
        if randint(1,10)<=3:
            egy_ugras=0
        ugrasok.append(egy_ugras)
    return ugrasok

def egy_versenyzo_kiirasa(rajtszam:int,ugrasok:list)->None:
    print(f'{rajtszam}. versenyzo ugrasai: ',end='')
    for ugras in ugrasok:
        if ugras==0:
            print('Érvénytelen',end=' ')
        else:
            print(ugras,end=' ')
    print(f'\n{rajtszam}. versenyzo legnagyobb ugrása: {versenyzo_legnagyobb_ugrasa (ugrasok)} m')

def versenyzo_legnagyobb_ugrasa(ugrasok:list)->float:
    #return max(ugrasok) # ez alapvizsgán nem biztos hogy jó (nem adnak pontot esetleg)
    max=0
    for ugras in ugrasok:
        if ugras>max:
            max=ugras
    return max
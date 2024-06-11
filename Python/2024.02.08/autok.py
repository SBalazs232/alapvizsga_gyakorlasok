from auto import auto

autok:list[auto]=[]

def betoltes(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    for sor in f:
        autok.append(auto(sor.strip()))
    f.close()

def autok_kiirasa(autolista:list[auto]):
    for a in autolista:
        print(f'{a.rendszam.ljust(10)} {a.marka.ljust(10)} {a.tipus.ljust(10)} {str(a.teljesitmeny).rjust(6)} {a.szin.ljust(10)}')

def autok_szin_alapjan(szin:str)->list[auto]:
    autok_uj_listaja=[]
    for a in autok:
        if a.szin.upper()==szin.upper():
            autok_uj_listaja.append(a)
    return autok_uj_listaja

def uj_auto_bekerese():
    print('Kérem adja meg az új autó adatait!\n')
    rendszam=input('Rendszám: ')
    marka=input('Márka: ')
    tipus=input('Tipus: ')
    teljesitmeny=input('Teljesítmény: ')
    szin=input('Szín: ')
    #eltároljuk a memóriában
    uj_auto=auto(rendszam+';'+marka+';'+tipus+';'+teljesitmeny+';'+szin)
    autok.append(uj_auto)

    #elmentjük a fájl végére
    f=open('autok.txt','a',encoding='UTF-8')
    f.write(rendszam+';'+marka+';'+tipus+';'+teljesitmeny+';'+szin+'\n')
    f.close()

def legerosebb_auto()->auto:
    legerosebb=autok[0]
    for a in autok[1:]:
        if a.teljesitmeny>legerosebb.teljesitmeny:
            legerosebb=a
    return legerosebb

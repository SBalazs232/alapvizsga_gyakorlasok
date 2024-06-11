from tanulo import *
from random import randint,choice

tanulok:list[tanulo]=[] #a tanulo osztály pédácson kerulnek
vezeteknevek = ['Kiss', 'Kovács', 'Szabó', 'Horváth', 'Fazekas', 'Török', 'Magyar']
keresztnevek = ['Márk', 'Bálint', 'Eszter', 'Judit', 'Elemér', 'Péter', 'Pál', 'Miksa', 'Töhötöm']

def uj_tanulo()->tanulo:
    vezeteknev=choice(vezeteknevek)
    keresztnev=choice(keresztnevek)
    szuletesi_ev=randint(2003,2010)
    szuletesi_honap=randint(1,12)
    szuletesi_nap=randint(1,28) #csak azért hogy ne kelljen vizsgálni a hónap alqapján - később meg lehet oldani
    szuletesi_datum=datetime(szuletesi_ev,szuletesi_honap,szuletesi_nap)
    jegyek=[]
    for i in range(randint(0,5)):
        jegyek.append(randint(1,5))
    return tanulo(vezeteknev,keresztnev,szuletesi_datum,jegyek)

def tanulok_feltolt(letszam:int)-> None:
    for i in range(letszam):
        tanulok.append(uj_tanulo()) #meghivjuk az uj tanulok fuggvenyt, majd a visszatérési értékét hozzáfűzzük a listához

def tanulok_kiir()-> None:
    for egytanulo in tanulok:
        print(f'{egytanulo.vezeteknev} {egytanulo.keresztnev} ({egytanulo.szuletes.strftime("%Y.%m.%d.")})')
        print(f'\tJegyei: {egytanulo.jegyek}')
        #print(f'\tJegyei: ',*egytanulo.jegyek)
        print(f'\tÁtlaga: {egytanulo.atlag():.2f} ') #tagfüggvény meghívása

def osztalyatlag()->float:
    osszeg=0
    db=0
    for egytanulo in tanulok:
        if egytanulo.atlag()>0:
            osszeg+=egytanulo.atlag()
            db+=1
    return osszeg/db

def atlag_folott_letszam()->int:
    db=0
    for egytanulo in tanulok:
        if egytanulo.atlag()>osztalyatlag():
            db+=1
    return db

def osztaly_legjobbja()->tanulo:
    legjobb=tanulok[0]
    for egytanulo in tanulok[1:]: #0dik indexűt kihagyjuk
        if egytanulo.atlag()>legjobb.atlag(): #ha talalunk jobbat
            legjobb=egytanulo
    return legjobb #visszatérunk a legjobb tanulo pédánnyal
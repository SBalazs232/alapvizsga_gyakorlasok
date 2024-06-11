from data import *

ubalaton:list[ultrabalaton]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding="UTF-8")
    f.readline()
    for sor in f:
        ubalaton.append(ultrabalaton(sor.strip()))
    f.close()

def kesz_noi_sportolo():
    db=0
    for u in ubalaton:
        if u.tavszazalek==100 and u.kategoria=='Noi':
            db+=1
    return db

def leghosszabb_nevu_futo():
    leghosszabb=''
    for u in ubalaton:
        if len(u.nev)>len(leghosszabb):
            leghosszabb==u
    return leghosszabb
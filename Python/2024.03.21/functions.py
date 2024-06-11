from data import *

szavazatok:list[eszemiszom]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    for sor in f:
        szavazatok.append(eszemiszom(sor))
    f.close()

def kepviselok_szama()->int:
    return len(szavazatok)

def kepviselo_kereses_korzetszama(k_nev:str)->int:
    sorszam=0
    for v in szavazatok:
        if v.nev==k_nev:
            
            sorszam+=v.sorszam
    return sorszam

def kepviselo_kereses_szavazata(k_nev:str)->int:
    kapott_szavazatok=0
    for v in szavazatok:
        if v.nev==k_nev:
            kapott_szavazatok+=v.szavazatok
    return kapott_szavazatok



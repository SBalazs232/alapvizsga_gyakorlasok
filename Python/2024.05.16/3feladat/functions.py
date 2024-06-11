from data import Festmeny

festmenyek:list[Festmeny]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        festmenyek.append(Festmeny(sor.strip()))
    f.close()

def festmenyek_szama():
    return len(festmenyek)

def kepszam_keresese_nev_alapjan(nev:str):
    db=0
    for f in festmenyek:
        if f.festo==nev:
            db+=1
    return db

def legdragabb_kep()->Festmeny:
    legdragabb=festmenyek[0]
    for festmeny in festmenyek[1:]:
        if festmeny.becsult_ar>legdragabb.becsult_ar:
            legdragabb=festmeny
    return legdragabb #ez egy osztálypéldány minden

def vanE()->bool:
    for festmeny in festmenyek:
        if festmeny.becsult_ar<=festmeny.eredeti_ar:
            return True
    return False
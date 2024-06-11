from data import eredmeny

eredmenyek:list[eredmeny]=[]

def fajlBeolvas(fajlnev):
    f=open(fajlnev,'r',encoding='UTF-8')
    for sor in f:
        eredmenyek.append(eredmeny(sor))
    f.close()

def helyezesek_szama(helyezes)->int:
    db=0
    for e in eredmenyek:
        if e.helyezes==helyezes:
            db+=1
    return db

def ossz_pont()->int:
    osszeg=0
    for e in eredmenyek:
        osszeg+=e.pont()
    return osszeg

def sportag_ermek(sportag)->int:
    db=0
    for e in eredmenyek:
        if e.sportag==sportag and e.helyezes<=3:
            db+=1
        return db
    
def fajl_bairas(fajlnev):
    f=open(fajlnev, 'w',encoding="UTF-8")
    for e in eredmenyek:
        if e.sportag=='kajakkenu':
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} kajak-kenu {e.versenyszam}\n')
        else:
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} {e.sportag} {e.versenyszam}\n')
    f.close()

def max_letszam()->eredmeny:
    legtobb=eredmenyek[0]
    for e in eredmenyek[1:]:
        if e.letszam>legtobb.letszam:
            legtobb=e
    return legtobb
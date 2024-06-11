from data import CBadás

cbadasok:list[CBadás]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    f.readline()
    for sor in f:
        cbadasok.append(CBadás(sor.strip()))
    f.close()

def bejegyzesek_szama():
    return len(cbadasok)

def nev_bejegyzesszam(nev:str):
    db=0
    for adas in cbadasok:
        if adas.nev==nev:
            db+=1
    return db

def maxadasdb(): #mennyi volt az 1 percben beluli legtobb adas
    max=0
    for adas in cbadasok:
        if adas.darab>max:
            max=adas.darab
    return max

def fajlbairas(fajlnev:str):
    f=open(fajlnev,'w',encoding='utf-8')
    f.write('kezdes;nev;adasdb')
    for adas in cbadasok:
        f.write(f'{adas.ora*60+adas.perc};{adas.nev};{adas.darab}\n')
    f.close()
from data import varos

varosok:list[varos]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    f.readline()
    for sor in f:
        varosok.append(varos(sor))
    f.close()

def varosok_szama()->int:
    return len(varosok)

def orszag_lakossaga(orszag:str)->int:
    osszeg=0
    for v in varosok:
        if v.orszag==orszag:
            osszeg+=v.lakossag
    return osszeg*1000 #mert itt nem 1000főbnen kérik hanem simán főben

def legnagyobb_varos()->varos:
    legnagyobb=varosok[0]
    for v in varosok[1:]:
        if v.lakossag>legnagyobb.lakossag:
            legnagyobb=v
    return legnagyobb

def orszag_keres(orszag:str)->bool:
    for v in varosok:
        if v.orszag==orszag:
            return True
    return False

def szokozos_varosook(szokozok_szama:int)->int:
    db=0
    for v in varosok:
        if v.szokozokdb()==szokozok_szama:
            db+=1
    return db #a paraméterként kapott tartalmazó városok száma

def orszag_statisztika()->dict[str,int]:
    stat:dict[str,int]={}
    for v in varosok:
        if v.orszag in stat.keys():
            stat[v.orszag]+=1
        else:
            stat[v.orszag]=1
    return stat 

def orszag_mentes(fajlnev:str,orszag:str):
    f=open(fajlnev,'w',encoding='UTF-8')
    for v in varosok:
        if v.orszag==orszag:
            f.write(f'{v.nev};{v.lakossag}\n')
    f.close()
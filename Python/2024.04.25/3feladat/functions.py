from data import Épület

epuletek:list[Épület]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        epuletek.append(Épület(sor.strip()))
    f.close()

def epuletek_szama():
    return len(epuletek)

def emelek_osszege():
    osszeg=0
    for epulet in epuletek:
        osszeg+=epulet.emeletek
    return osszeg

def legamagasabb_epulet():
    leg=epuletek[0]
    for epulet in epuletek[1:]:
        if epulet.magassag>leg.magassag:
            leg=epulet
    return leg

def orszag_keres(orszag:str):
    for e in epuletek:
        if orszag == e.orszag:
            return True
    return False
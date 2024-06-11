from data import fogadasi_fordulo

fordulok:list[fogadasi_fordulo]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    f.readline()
    for sor in f:
        fordulok.append(fogadasi_fordulo(sor))
    f.close()

def fordulokszama()->int:
    return len(fordulok)

def telitalalatosok_szama()->int:
    db=0
    for fordulo in fordulok:
        db+=fordulo.t13t1
    return db

def dontetlen_e()->bool:
    for f in fordulok:
        if 'X' not in f.eredmenyek:
            return True
    return False
            
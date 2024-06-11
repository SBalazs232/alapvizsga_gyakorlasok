from data import foci

focivb:list[foci]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF-8')
    f.readline()
    for sor in f:
        focivb.append(foci(sor))
    f.close()

def csapatok_szama()->int:
    return len(focivb)

def vb_2018():
    for f in focivb:
        if f.legutobbi_reszvetel==2018:
            print(f.csapat)

def benelux_orszagok()->int:
    reszvetel=0
    for f in focivb:
        if "Hollandia"==f.csapat:
            reszvetel+=f.reszvetelek_szam
        elif "Belgium"==f.csapat:
            reszvetel+=f.reszvetelek_szam
        elif "Luxemburg"==f.csapat:
            reszvetel+=f.reszvetelek_szam
    return reszvetel

def elso_vb()->int:
    legelso_vb=str(focivb[2])
    for f in focivb:
        if f.elso_reszvetel<legelso_vb:
            legelso_vb=f.elso_reszvetel
    return legelso_vb

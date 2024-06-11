nevek=['Magdics Áron','Melecky Ambrus','Nagy Péter','Nagy Rómeó','Németh Bence','Novák Maja','Papp Bence Csanád','Pram Bertalan','Sághi Szilárd','Sári Balázs','Simon Kristóf','Steingart Erik','Szabó Zsombor','Szaszák Péter','Szeiber Péter','Tóth Benedek','Vanyus Domonkos']

def csoport_letszam()->int:
    return len(nevek)

def leghosszabb_nev_hossza()->int:
    hossz=0
    for nev in nevek:
        if len(nev)>hossz:
            hossz=len(nev)
    return hossz

def atlagos_nev_hossz()->float:
    osszeg=0
    for nev in nevek:
        osszeg+=len(nev)
    return osszeg/len(nevek)
def nev_kereses(keresett:str)->bool:
    for nev in nevek:
        if nev == keresett:
            return True
    return True
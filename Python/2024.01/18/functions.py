versenyzok=['BASTIEN Steven', 'dos SANTOS Felipe', 'DUBLER Cedric', 'ERM Johannes', 'HELCELET Adam Sebastian', 'KAZMIREK Kai', 'LEPAGE Pierce', 'MAYER Kevin', 'MOLONEY Ashley', 'ROE Martin', 'SCANTLING Garrett', 'SHKURENYOV Ilya', 'SYKORA Jiri', 'TILGA Karel', 'UIBO Maicel', 'URENA Jorge', 'VICTOR Lindon', 'WARNER Damian', 
'WIESIOLEK Pawel', 'ZHUK Vitaliy', 'ZIEMEK Zachery']

pontok=[8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 8413, 7943, 7018, 8037, 8322, 8414, 9018, 8176, 8131, 8435]

def resztvevok_szama()->int:
    return len(versenyzok)

def pontnal_nagyobb(pont)->int:
    db=0
    for p in pontok:
        if p>=pont: #ha a versenyző pontja nagyobb,mint a paraméterként kapott pontérték
            db+=1
    return db

def pont_atalg()->float:
    osszeg=0
    for p in pontok:
        osszeg+=p
        return osszeg/len(pontok)

def gyoztes_indexe()->int:
    gyoztes=0
    for i in range(1,len(pontok)):
        if pontok[i]>pontok[gyoztes]:
            gyoztes=i
    return gyoztes

def versenyzo_pontja(nev:str)->int|bool:
    for i in range(len(versenyzok)):
        if versenyzok[i]==nev:
            return pontok[i]
    return False
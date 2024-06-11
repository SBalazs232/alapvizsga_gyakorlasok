class foci:
    def __init__(self,sor:str) -> None:
        adatok=sor.strip().split(';')
        self.csapat=adatok[0]
        self.reszvetelek_szam=int(adatok[1])
        self.elso_reszvetel=adatok[2]
        self.legutobbi_reszvetel=int(adatok[3])
        self.legjobb_eredmeny=adatok[4]
class ultrabalaton:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=str(adatok[0])
        self.rajtszam=int(adatok[1])
        self.kategoria=adatok[2]
        self.ido=adatok[3]
        self.tavszazalek=int(adatok[4])
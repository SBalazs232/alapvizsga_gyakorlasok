
class auto:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.rendszam=adatok[0]
        self.marka=adatok[1]
        self.tipus=adatok[2]
        self.teljesitmeny=float(adatok[3])
        self.szin=adatok[4]
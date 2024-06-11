class eszemiszom:
    def __init__(self,sor:str) -> None:
        adatok=sor.strip().split(' ')
        self.sorszam=int(adatok[0])
        self.szavazatok=int(adatok[1])
        self.vezeteknev=adatok[2]
        self.utonev=adatok[3]
        self.nev=adatok[2]+' '+adatok[3]
        self.part=adatok[4]
'''
class auto: #osztály - 1 példány adatai kerülnek bele
    tipus=''
    renszam=''
    szin=''
    teljesitmeny=''
    gyorsulas=""
'''

class auto:
    def __init__(self,tipus:str,rendszam:str,teljesitmeny:float,szin:str,gyorsulas:float=0) -> None: #a koonstruktor megadása ami egy speciális fuggvény
        #lehetnek metódusok (az osztály saját függvényei)
        #a példányosíáskor fut le
        #self - hivatkozás a saját osztályra, minden metódus 1. paramétere ez kell, hogy legyen!!!
        #gyorsulásnál  - alapértelmezett értéke a 0
        self.tipus=tipus
        self.rendszam=rendszam
        self.szin=szin
        self.tejesitmeny=teljesitmeny
        self.gyorsulas=gyorsulas


from random import randint

versenyzo_pontjai=[] # osszes versenyzo

versenyzok_osszpontszama=[] #osszes versenyzo


def random_pontszam()->float:
    #return randint(0,9)+randint(0,4)/4
    return randint(0,40)/4

def versenyzo_pontjai()->list[float]:
    pontszamok=[]
    for i in range(7):
        pontszamok.append(random_pontszam())
    return pontszamok

def legalacsonyabb_pont(pontszamok)->float:
    return min(pontszamok)

def gyoztes_versenyzo_sorszama()->int:
    max_sorszam=0
    max_pont=0
    for i in range(len(versenyzok_osszpontszama)):
        if versenyzok_osszpontszama[i]>max_pont:
            max_pont=versenyzok_osszpontszama[i]
            max_sorszam=i
    return max_sorszam+1

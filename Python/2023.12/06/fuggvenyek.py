# mire használjuk a függvényeket:
 #olyan kis programegységek, amelyeket változatos bemeneti adatokkal (paraméterek) szeretnénk végre hajtani, akért sokszpr is
 #cél az ujra hasznosithatosag!!
#mit kell tudni a fuugvenyekrol
# - mit csinal a fuggveny ( a neve utaljon a megvalositott feladatra)
# - mi a fgv. paraméterlistája (neve után zárojelben felsoorolt változók)
# - formális paraméterei (neve mogott zárojelben megadott változó nevek esetleg tipusai)
# - aktualis parameterlista (a fgv.hívasakor a fgv.nek adott konkret ertek /ez lehet valtozo is/)
# -  mit ad vissza eredményul (return kulcsszo utani ertek)
# a fgv. CSAK a meghivasakor fut le!! letrehozasakor (deklaracio) csak letrejon de nem hajt vegre!

#def osszeg(a,b): #a es b fromalis parameterek
def osszeg(a:float,b:float)->float: #tipus megadas
    #print(a+b) nem kirini szeretnent
    osszeg=a+b #fgv magja
    return a+b #hanem visszaadni
    print('ami a return utan van az nem hajtodik vegre egy ezt soha nem fogjuk latni')
print(osszeg(10,30)) #10,30 aktualis parameterek
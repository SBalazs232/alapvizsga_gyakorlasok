#kup felszin térfogat számítása
#sugarát bekérjük és a magasságát

from math import sqrt, pow, pi
#sqrt - gyök 2
#pow hatvany
#pi-pi

r=float(input("Adja meg a kúp alapjának sugarát: "))
h=float(input("Adja meg a kúp alapjának magasságát: "))

a=sqrt(pow(r,2)+pow(h,2)) #rnégyzet + h négyzet
#a=sqrt(r**2+h**2)    ugyan az

A=r**2*pi+r*pi*a #alap területe + a palást területe
A=round(r**2*pi+r*pi*a,2) #kerekites (mit, hany tizedes pontossaggal)

V=r**2*pi*h/3

print(f"Felszín: {A}")
print(f"Tpérfogat: {V:.2f}") #ugayn az mint a kerekites
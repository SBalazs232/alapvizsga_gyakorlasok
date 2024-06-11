#kérjük be két pont koordinátáit
#mondjuk meg a 2 pont távolságát
#P1(5,3) - P1(x1,y1)
#P2(-3,1) - P2(x2,y2)
from math import sqrt

x1=int(input("Az első pont x koordinátája: "))
y1=int(input("Az első pont y koordinátája: "))
x2=int(input("A második pont x koordinátája: "))
y2=int(input("A második pont y koordinátája: "))

tavolsag=sqrt((x1-x2)**2+(y1-y2)**2)

print(f"A két pont távolsága: {tavolsag}")
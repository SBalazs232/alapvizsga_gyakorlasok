import math #matek fugvenyek hasznalatahoz


a_oldal = int(input("a= "))
b_oldal = int(input("b= "))
c_oldal = int(input("c= "))

"""
logikai operatotk
ÉS - and             -minden feltételmnek teljesulnie kell
VAGY- or               -legalabb 1nek
TAGADÁS - not
"""

if((a_oldal+b_oldal)>c_oldal) and ((a_oldal+c_oldal)>b_oldal) and ((b_oldal+c_oldal)>a_oldal):
    kerulet=a_oldal+b_oldal+c_oldal
    s=kerulet/2
    terulet=math.sqrt(s*(s-a_oldal)*(s-b_oldal)*(s-c_oldal))
    print(f"kerulet: {kerulet}")
    print(f"terulet: {terulet:.2f}")


else:
    print("nem szerkesztheto meg")
#kérjük be egy másodfokú együtthatóit (a,b,c)
#Írjuk ki a gyökeit a valós számok halmazán.

from math import sqrt #négyzetgyök

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

d=b**2-4*a*c  #diszkrimináns

if d>=0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b+sqrt(d))/(2*a)
    print(f"x1={x1}")
    print(f"x2={x2}")
else:
    print("nincs megoldás a valós számok halmazán")

 
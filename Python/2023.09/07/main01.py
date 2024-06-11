#egy soros komment
"""
több soros komment
asdadfaw
ctrl+k+c (komment)
ctrl+k+u (unkomment)
"""

print("alam lalam")
szam="pofefens"
print(szam)
print(type(szam))

a=10
b=5
c=a+b
print(c*a)
print((a+b)*a)
print('c=' + str(a+b))
print(f'c={a+b}')
print(f'{a} + {b} = {c}')

#változonevekkel kapcsolatos szabalyok

#1péter nem kezdőthet számmal
#péter neve nem lehet benne szóköz
#peter's name nem lehet benne speciális karkter
# csqak 0-9 vagy A-6Z vagy a-z vagy _
péter1=12 #ez jo!
péter_neve="Péter" # ez jo!!

#-------------------------------------------------------------------------
#mire figyeljunk hogy ne kapjunk 1est
#asd=12 - TILOS
#a=5 vagy b=12 helyette a_oldal=5 vagy b_oldal
#torekedjunk arra hogy felismerhető legyen hogy mit tárolunk bennük


#-------------------------------------------------------------------------
#autó adatai (típus, tulajdonos):
auto_tipus="Opel"
auto_tulajdonos="Pop Simon"    #nake case (_ alulvonas)

autoTipus="Audi"    #camel case

AutoTipus="Audi"    #Pascal case

#--------------------------------------------------------------------------

print("\t tabulatorral kezdodo sor" , end='')
print("\t\t ketto tablator")
print("\n\n sor emeles \n \t uj sor")

print("alma","korte","banana","szilva" ,sep=', ' , end=", ")
print("narancs" , end='!')

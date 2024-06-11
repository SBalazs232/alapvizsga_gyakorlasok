from auto import auto

# az_en_autom=auto #példányosítás (1.db obj. példány jön létre)
# az_en_autom.rendszam='AA-AA-001'
# az_en_autom.szin='kék'
# az_en_autom.tipus='Ford'
# az_en_autom.teljesitmeny=100

# szomszed_autoja=auto
# az_en_autom.rendszam='BE-NI-007'
# az_en_autom.szin='zöld'
# az_en_autom.tipus='Suzuki'
# az_en_autom.teljesitmeny=2

# print(szomszed_autoja.rendszam)

autok:list[auto]=[] #az autok egy olyan lista, amelyben auto osztálypéldányok lesznek

egy_auto=auto('Skoda','BE-NI-007',1000,'Szürke',0.9)
autok.append(egy_auto)

autok.append(auto('Skoda','BE-NI-007',1000,'Szürke',0.9))
autok.append(auto('Trabant','BA-LI-888',1200,'Baba Kék',0.1))
autok.append(auto('Lada','EE-NI-009',1000,'Paradicsom Piros',0.3))

#print(autok[0].tipus)

#teljes lista kiirasa - sorszammal

for i in range(len(autok)):
    print(f'{i+1}. {autok[i].tipus.ljust(10)} {autok[i].rendszam.ljust(10)} {autok[i].szin.ljust(10)} {str(autok[i].tejesitmeny).ljust(10)} {str(autok[i].gyorsulas).ljust(4)}')

#teljes lista kiirasa - ha nem kell sorszam
for a in autok:
        print(f'{a.tipus.ljust(10)} {a.rendszam.ljust(10)} {a.szin.ljust(10)} {str(a.tejesitmeny).ljust(10)} {str(a.gyorsulas).ljust(4)}')

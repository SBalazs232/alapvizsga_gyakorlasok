ma_ev=2023
ma_honap=9
ma_nap=14

szuletesi_datum=input("születési dátum (éééé.hh.nn): ")

(szuletesi_ev,szuletesi_honap,szuletesi_nap)=szuletesi_datum.split(".")

szuletesi_ev=int(szuletesi_ev)
szuletesi_honap=int(szuletesi_honap)
szuletesi_nap=int(szuletesi_nap)

"""
logikai valtozok lehetseges erterkei
False- hamis
True-igaz
"""

elmult_18=False #kezdetben elmult 18 eves

if ma_ev-szuletesi_ev>18:
    elmult_18=True #átbillen igazra
elif ma_ev-szuletesi_ev==18:
    if ma_honap>szuletesi_honap:
        elmult_18=True
    elif ma_honap==szuletesi_honap:
        if ma_nap>szuletesi_nap:
            elmult_18=True

if elmult_18:      #ez ugyanaz min elmult_18==True
    print("vehetsz")
else:
    print("nem vehetsz")
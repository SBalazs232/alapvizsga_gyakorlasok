#döntsül el hogy vehet-e alkoholt vagy nem



ma_ev=2023
ma_honap=9
ma_nap=14

szuletesi_ev=int(input("szuletesi eve: "))

if ma_ev-szuletesi_ev<18:
    print("nem v ejhet alkoholt")
elif ma_ev-szuletesi_ev>18:
    print("vehet alkoholt")
else:
    szuletesi_honap=int(input("szuletesi honapja: "))
    if ma_honap<szuletesi_honap:
        print("nem kapsz alkoholt")
    elif ma_honap>szuletesi_honap:
        print("vehetsz")
    else:
        szuletesi_nap=int(input("szuletesi napod: "))
        if ma_nap<szuletesi_nap:
            print("nem vehetsz")
        elif ma_nap>szuletesi_nap:
            print("vehetsz")
        else:
            print("vehetsz, boldog születésnapot!")
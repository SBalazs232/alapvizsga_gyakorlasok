nev='na' #bármi legyen benne

while nev!='': #amikor ures stringet kap akkor kilep
    nev=input("Név: ")
    if nev!='':
        kegoria=int(input("Ketageória: "))
        koltseg=int(input("koltseg: "))

        limit=kegoria*10000
        if koltseg>limit:
            print(f"{nev}: {koltseg-limit} Ft")
        else:
            print(f"{nev}: nincs onkoltseg")

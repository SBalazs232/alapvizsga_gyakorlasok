print("Abszolút érték\n")

szam=float(input("Szám: "))
#összehasonlito operatorok:
#< - kisebb
#<= - kisebb egyenlő
#>= - nagyobb egyenlo
#> - nagyobb
#!= - nem egysenlo

if szam>=0:
    print(f" A szám abszoéut erteke: {szam}")
else:
    #print(f" a szam abszolut erteke: {szam*-1}")
    print(f" a szam abszolut erteke: {-szam}")
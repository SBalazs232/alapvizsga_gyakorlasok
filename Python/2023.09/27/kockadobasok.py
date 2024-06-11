#dobjunk 1db hagyományos dobókockával valahányszor
#v1:Mondjuk meg hány darab hatos dobas volt
#v2: melyikbol mennyi volt - statisztika

from random import randint

n=20 #dobasok szama

egyesek_szama=0
kettesek_szama=0
harmasok_szama=0
negyesek_szama=0
otosok_szama=0
hatosok_szama=0

for i in range(n):
    dobas=randint(1,6)
    print(dobas, end=" ")
    # if dobas==1:
    #     egyesek_szama+=1
    # elif dobas==2:
    #     kettesek_szama+=1
    # elif dobas==3:
    #     harmasok_szama+=1
    # elif dobas==4:
    #     negyesek_szama+=1
    # elif dobas==5:
    #     otosok_szama+=1
    # else:
    #     hatosok_szama+=1

    match dobas:
        case 1: egyesek_szama+=1
        case 2: kettesek_szama+=1
        case 3: harmasok_szama+=1
        case 4: negyesek_szama+=1
        case 5: otosok_szama+=1
        case 6: hatosok_szama+=1
        #case _: #akkor fut le, ha a fenti esetek egyike sem teljesül
         

print(f"\n\nEgyes dobások száma: {egyesek_szama}")
print(f"Kettes dobások száma: {kettesek_szama}")
print(f"Hármas dobások száma: {harmasok_szama}")
print(f"Négyes dobások száma: {negyesek_szama}")
print(f"Ötös dobások száma: {otosok_szama}")
print(f"Hatos dobások száma: {hatosok_szama}")
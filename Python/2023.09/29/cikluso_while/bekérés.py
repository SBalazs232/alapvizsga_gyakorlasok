#ellenőrzött bekérés (még ne, lesz tökéletes majd később tovább fejlesztjük)

#kérjünk be egy számot 10 és 100 között, a bekérést ismételjuk addig amig NEM jó értéket ad meg

szam=-1 #olyan kezdoertek amely először teljesíti a while feltételét

while szam<10 or szam>100:
    #szam=int(input("adjon meg egy számmot 10 és 100 között: "))
    input_txt=input("adjon meg egy számmot 10 és 100 között: ")
    if input_txt.isnumeric():   #csak szamjegyeket fogad el, 0 agy pozitiv egesz szam
        szam=int(input_txt)
    else:
        print("Egész számot adjon meg!")

    #később float input saját fuggvenyel
    #int input ---> saját fgv. negativ is lehet majd
        
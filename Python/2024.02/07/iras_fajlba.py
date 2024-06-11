zoldseg=input('adja meg a zöldség nevét: ')

#fajl=open('zoldsegek.txt','w',encoding='UTF-8')
#'w' write 
# ha nem létezik létre hozza ha létezik felülírja


fajl=open('zoldsegek.txt','a',encoding='UTF-8')
#'a' append 
# ha nem létezik létre hozza ha létezik beleír a végéhez0

fajl.write('\n'+zoldseg)

zoldsegek=['hagyma','zeller','cékla','karfiol','']
#soronként fáljba írása
for zoldseg in zoldsegek:
    fajl.write('\n'+zoldseg)

fajl.close()

